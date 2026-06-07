#!/usr/bin/env python3
"""NotebookLM tarzı podcast üreticisi (Gemini çok-sesli TTS).

`podcast_script_TR.md` içindeki "**ELA:** ..." / "**CAN:** ..." diyaloğunu
okur ve Gemini'nin çok-sesli text-to-speech modeliyle tek bir WAV dosyasına
seslendirir.

NEDEN BU AYRI BİR SCRIPT?
  Bu repo'nun çalıştığı bulut ortamında ağ erişimi izin listesiyle sınırlı
  olduğundan TTS API'sine doğrudan ulaşılamıyor. Bu dosyayı ağ erişimi olan
  bir makinede (ya da CI'da, gerekli host'lar allowlist'e eklenerek) çalıştırın.

KURULUM:
  pip install google-genai
  export GEMINI_API_KEY=...      # https://aistudio.google.com/app/apikey

KULLANIM:
  python generate_audio.py                      # podcast_script_TR.md -> podcast_TR.wav
  python generate_audio.py --script bolum2.md --out bolum2.wav

NOTLAR:
  - Gemini çok-sesli TTS en fazla 2 konuşmacı destekler; bu senaryoda
    ELA ve CAN olmak üzere tam 2 konuşmacı var.
  - Çıktı 24 kHz, 16-bit, mono PCM'dir; aşağıda WAV başlığıyla sarılır.
  - Çok uzun senaryolarda tek istekte token sınırına takılırsanız, senaryoyu
    parçalara bölüp üretilen WAV'ları birleştirin (örn. ffmpeg ile).
"""

from __future__ import annotations

import argparse
import os
import re
import struct
import sys
import wave
from pathlib import Path

# Konuşmacı -> Gemini ön-ayar ses adı eşlemesi.
# Mevcut sesler için: https://ai.google.dev/gemini-api/docs/speech-generation
VOICES = {
    "ELA": "Kore",      # canlı, meraklı ton
    "CAN": "Puck",      # sıcak, açıklayıcı ton
}

MODEL = "gemini-2.5-flash-preview-tts"
SPEAKER_RE = re.compile(r"^\*\*([A-ZÇĞİÖŞÜ]+):\*\*\s*(.+)$")


def parse_dialogue(md_path: Path) -> list[tuple[str, str]]:
    """Markdown senaryosundan (konuşmacı, replik) çiftlerini çıkarır."""
    turns: list[tuple[str, str]] = []
    for line in md_path.read_text(encoding="utf-8").splitlines():
        m = SPEAKER_RE.match(line.strip())
        if m:
            speaker, text = m.group(1), m.group(2).strip()
            if speaker in VOICES and text:
                turns.append((speaker, text))
    if not turns:
        sys.exit(f"Hata: {md_path} içinde '**ELA:** ...' biçiminde diyalog bulunamadı.")
    return turns


def build_prompt(turns: list[tuple[str, str]]) -> str:
    """TTS modeline tek seferde verilecek, konuşmacı etiketli düz metin."""
    header = (
        "Read aloud the following two-host Turkish science podcast in a warm, "
        "natural, conversational tone. Keep a lively back-and-forth rhythm:\n\n"
    )
    body = "\n".join(f"{spk}: {txt}" for spk, txt in turns)
    return header + body


def write_wav(pcm: bytes, out_path: Path, rate: int = 24000) -> None:
    with wave.open(str(out_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)   # 16-bit
        wf.setframerate(rate)
        wf.writeframes(pcm)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--script", default="podcast_script_TR.md", help="Girdi Markdown senaryosu")
    ap.add_argument("--out", default="podcast_TR.wav", help="Çıktı WAV dosyası")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Hata: GEMINI_API_KEY ortam değişkeni ayarlı değil.")

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("Hata: 'pip install google-genai' çalıştırın.")

    here = Path(__file__).parent
    md_path = (here / args.script) if not Path(args.script).is_absolute() else Path(args.script)
    turns = parse_dialogue(md_path)
    prompt = build_prompt(turns)
    print(f"{len(turns)} replik okundu. Ses üretiliyor ({MODEL})...")

    client = genai.Client(api_key=api_key)
    speaker_cfgs = [
        types.SpeakerVoiceConfig(
            speaker=name,
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name=voice)
            ),
        )
        for name, voice in VOICES.items()
    ]

    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                    speaker_voice_configs=speaker_cfgs
                )
            ),
        ),
    )

    pcm = resp.candidates[0].content.parts[0].inline_data.data
    out_path = (here / args.out) if not Path(args.out).is_absolute() else Path(args.out)
    write_wav(pcm, out_path)
    print(f"Bitti: {out_path}  ({len(pcm) / 1024:.0f} KB PCM)")


if __name__ == "__main__":
    main()
