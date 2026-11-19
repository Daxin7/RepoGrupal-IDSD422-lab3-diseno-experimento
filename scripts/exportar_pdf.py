# exportar_pdf.py — Exporta plantilla-encuesta.md a informes/plantilla-encuesta.pdf.
#
# La carátula toma el encabezado de la plantilla (todo lo que está antes de la
# primera línea "---"), incluido el enlace del fork. Requiere pandoc (viene con
# Quarto) y Microsoft Edge o Google Chrome para imprimir el HTML a PDF.
#
# Uso (desde la raíz del repositorio):
#   python scripts/exportar_pdf.py

import shutil
import subprocess
import tempfile
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "plantilla-encuesta.md"
SALIDA = RAIZ / "informes" / "plantilla-encuesta.pdf"

CANDIDATOS_PANDOC = [
    shutil.which("pandoc"),
    r"C:\Program Files\Quarto\bin\tools\pandoc.exe",
]
CANDIDATOS_NAVEGADOR = [  # Chrome primero: Edge a veces termina antes de escribir el PDF
    shutil.which("chrome"), shutil.which("google-chrome"),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    shutil.which("msedge"),
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

CSS = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm;
        @bottom-right { content: counter(page); font: 9pt 'Segoe UI', sans-serif; color: #777; } }
@page :first { @bottom-right { content: none; } }
body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10.5pt;
       line-height: 1.45; color: #1d2733; }
h1, h2, h3 { font-family: Georgia, 'Times New Roman', serif; color: #17324d; }
h2 { font-size: 15pt; border-bottom: 2px solid #c9a227; padding-bottom: 3px;
     margin-top: 22px; break-after: avoid; }
h3 { font-size: 12pt; margin-top: 16px; break-after: avoid; }
p, li { text-align: left; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9pt;
        break-inside: auto; }
tr { break-inside: avoid; }
th { background: #17324d; color: #fff; text-align: left; }
th, td { border: 1px solid #c8d0da; padding: 4px 6px; vertical-align: top; }
tbody tr:nth-child(even) td { background: #f4f6f9; }
code { font-family: Consolas, 'Courier New', monospace; font-size: 9pt;
       background: #eef1f5; padding: 0 3px; border-radius: 3px; }
pre { background: #f4f6f9; border: 1px solid #d5dbe3; border-radius: 4px; padding: 8px;
      white-space: pre-wrap; word-break: break-word; font-size: 8.6pt; break-inside: avoid; }
pre code { background: none; padding: 0; }
hr { border: none; border-top: 1px solid #c8d0da; margin: 18px 0; }
a { color: #17324d; }
.caratula { break-after: page; text-align: center; padding-top: 40mm; }
.caratula .inst { letter-spacing: 3px; font-weight: 700; color: #17324d; font-size: 13pt; }
.caratula .fac { color: #555; font-size: 10.5pt; margin-top: 4px; }
.caratula .barra { width: 70px; height: 4px; background: #c9a227; margin: 18px auto; border-radius: 2px; }
.caratula .tag { color: #9a7b14; font-size: 9pt; letter-spacing: 1.5px; font-weight: 700; }
.caratula h1 { font-size: 22pt; margin: 8px 0 26px; }
.caratula .meta { display: inline-block; text-align: left; font-size: 11pt; line-height: 1.6;
                  border-top: 1px solid #c8d0da; padding-top: 14px; max-width: 150mm; }
.caratula .meta ul { margin: 0 0 0 4px; }
.caratula .fork { margin-top: 18px; padding: 8px 12px; border: 1.5px solid #17324d;
                  border-radius: 6px; font-size: 11pt; text-align: center; }
"""


def encontrar(candidatos, nombre):
    for ruta in candidatos:
        if ruta and Path(ruta).exists():
            return ruta
    raise SystemExit(f"No se encontró {nombre}.")


def a_html(pandoc, markdown):
    return subprocess.run([pandoc, "-f", "gfm", "-t", "html"], input=markdown,
                          capture_output=True, text=True, encoding="utf-8", check=True).stdout


pandoc = encontrar(CANDIDATOS_PANDOC, "pandoc")
navegador = encontrar(CANDIDATOS_NAVEGADOR, "Edge o Chrome")

texto = FUENTE.read_text(encoding="utf-8").replace("\r\n", "\n")
encabezado, cuerpo = texto.split("\n---\n", 1)
titulo, meta = encabezado.split("\n", 1)
repositorio = next(l for l in meta.splitlines() if l.startswith("**Repositorio"))
meta = meta.replace(repositorio + "\n", "")
enlace = repositorio.split(":**", 1)[1].strip()

html = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>{titulo.lstrip('# ')}</title><style>{CSS}</style></head><body>
<section class="caratula">
  <div class="inst">ESCUELA POLITÉCNICA NACIONAL</div>
  <div class="fac">Facultad de Ingeniería de Sistemas · Carrera de Ciencia de Datos e Inteligencia Artificial</div>
  <div class="barra"></div>
  <div class="tag">PRÁCTICA 2 (TÓPICO 2) · HITO 1 · ENTREGA FINAL</div>
  <h1>{titulo.lstrip('# ')}</h1>
  <div class="meta">{a_html(pandoc, meta)}
    <div class="fork"><strong>Repositorio (fork):</strong> <a href="{enlace}">{enlace}</a></div>
  </div>
</section>
{a_html(pandoc, cuerpo)}
</body></html>"""

SALIDA.parent.mkdir(exist_ok=True)
SALIDA.unlink(missing_ok=True)
with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
    pagina = Path(tmp) / "plantilla.html"
    pagina.write_text(html, encoding="utf-8")
    subprocess.run([navegador, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--user-data-dir={Path(tmp) / 'perfil'}",
                    f"--print-to-pdf={SALIDA}", pagina.as_uri()],
                   check=True, capture_output=True, timeout=120)
    for _ in range(60):  # espera a que el navegador termine de escribir
        if SALIDA.exists() and SALIDA.stat().st_size > 0:
            break
        time.sleep(1)
    else:
        raise SystemExit("El navegador no generó el PDF.")
print(f"PDF generado: {SALIDA.relative_to(RAIZ)} ({SALIDA.stat().st_size / 1024:.0f} KB)")
