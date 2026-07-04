from pathlib import Path

original = Path("StarFoxZeroTranslation/Original")
translated = Path("StarFoxZeroTranslation/Traduzido")

extensions = {".txt", ".json", ".xml", ".csv"}

total = sum(
    1 for f in original.rglob("*")
    if f.is_file() and f.suffix.lower() in extensions
)

done = sum(
    1 for f in translated.rglob("*")
    if f.is_file() and f.suffix.lower() in extensions
)

remaining = total - done
percent = 0 if total == 0 else done / total * 100

size = 20
filled = round(size * percent / 100)

bar = "🟩" * filled + "⬜" * (size - filled)

progress = f"""
## 📊 Status da Tradução

### 🟢 Progresso Geral

**{percent:.2f}%**

{bar}

<progress value="{done}" max="{total}"></progress>

| 📁 Estatística | Quantidade |
|---------------|-----------:|
| ✅ Traduzidos | **{done:,}** |
| ⏳ Restantes | **{remaining:,}** |
| 📦 Total | **{total:,}** |
"""

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

start = "<!-- PROGRESS_START -->"
end = "<!-- PROGRESS_END -->"

before = text.split(start)[0]
after = text.split(end)[1]

readme.write_text(
    before + start + "\n" + progress + "\n" + end + after,
    encoding="utf-8"
)