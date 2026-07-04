from pathlib import Path

original = Path("Original")
translated = Path("Traduzido")

# extensões que serão consideradas
extensions = {".csv"}

total = sum(1 for f in original.rglob("*") if f.is_file() and f.suffix.lower() in extensions)
done = sum(1 for f in translated.rglob("*") if f.is_file() and f.suffix.lower() in extensions)

percent = 0 if total == 0 else done / total * 100

# Barra de progresso
size = 30
filled = int(size * done / total) if total else 0
bar = "█" * filled + "░" * (size - filled)

progress = f"""### 📊 Status da Tradução

**{percent:.2f}%**

{bar}

**{done} / {total} arquivos traduzidos**
"""

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

start = "<!-- PROGRESS_START -->"
end = "<!-- PROGRESS_END -->"

before = text.split(start)[0]
after = text.split(end)[1]

new_text = before + start + "\n" + progress + "\n" + end + after

readme.write_text(new_text, encoding="utf-8")
