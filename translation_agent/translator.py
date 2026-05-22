#!/usr/bin/env python3
"""
🌐 Meeting Translation Agent
İngilizce ↔ Türkçe Anlık Çeviri Ajanı

Bu program online toplantılarda İngilizce metni Türkçeye,
Türkçe cevaplarınızı İngilizceye çevirir.
"""

import anthropic
import sys


def translate_english_to_turkish(text: str, client: anthropic.Anthropic) -> str:
    """İngilizce metni Türkçeye çevir"""
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Lütfen aşağıdaki İngilizce metni Türkçeye çevir.
Sadece çeviriyi ver, başka şey yazma.

İngilizce: {text}

Türkçe:""",
            }
        ],
    )
    return message.content[0].text.strip()


def translate_turkish_to_english(text: str, client: anthropic.Anthropic) -> str:
    """Türkçe metni İngilizceye çevir"""
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Lütfen aşağıdaki Türkçe metni İngilizceye çevir.
Sadece çeviriyi ver, başka şey yazma.

Türkçe: {text}

English:""",
            }
        ],
    )
    return message.content[0].text.strip()


def main():
    """Ana program"""
    # API anahtarını al
    api_key = sys.argv[1] if len(sys.argv) > 1 else None

    if not api_key:
        print("❌ Hata: Claude API anahtarı gerekli!")
        print("\nKullanım:")
        print("  python translator.py YOUR_API_KEY")
        print("\nAPI anahtarını buradan al: https://console.anthropic.com/")
        sys.exit(1)

    # Claude client'ını oluştur
    client = anthropic.Anthropic(api_key=api_key)

    print("🌐 Meeting Translation Agent")
    print("=" * 50)
    print("İngilizce ↔ Türkçe Çeviri Ajanı\n")
    print("Komutlar:")
    print("  'en' - İngilizce metni Türkçeye çevir")
    print("  'tr' - Türkçe metni İngilizceye çevir")
    print("  'exit' - Çıkış\n")

    while True:
        try:
            print("-" * 50)
            mode = input("\n📝 Mod seçin (en/tr/exit): ").strip().lower()

            if mode == "exit":
                print("👋 Hoşça kalın!")
                break

            if mode == "en":
                text = input("🇬🇧 İngilizce metni gir: ").strip()
                if text:
                    print("\n⏳ Çeviriliyor...")
                    result = translate_english_to_turkish(text, client)
                    print(f"\n🇹🇷 Türkçe:\n{result}")

            elif mode == "tr":
                text = input("🇹🇷 Türkçe metni gir: ").strip()
                if text:
                    print("\n⏳ Çeviriliyor...")
                    result = translate_turkish_to_english(text, client)
                    print(f"\n🇬🇧 English:\n{result}")

            else:
                print("❌ Geçersiz mod! 'en', 'tr' veya 'exit' yazın.")

        except KeyboardInterrupt:
            print("\n\n👋 Program durduruldu.")
            break
        except anthropic.APIError as e:
            print(f"❌ API Hatası: {e}")
            print("API anahtarını kontrol edin!")
            break


if __name__ == "__main__":
    main()
