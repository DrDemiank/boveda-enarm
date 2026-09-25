
S_TERMINAL = ("ellipse;whiteSpace=wrap;html=1;"
              "fillColor=#000000;strokeColor=#000000;"
              "fontColor=#FFFFFF;fontStyle=1;fontSize=13;")
S_PROCESS  = ("rounded=1;whiteSpace=wrap;html=1;"
              "fillColor=#FFFFFF;strokeColor=#000000;"
              "fontColor=#000000;fontStyle=0;fontSize=11;")
S_DECISION = ("rhombus;whiteSpace=wrap;html=1;"
              "fillColor=#FFFFFF;strokeColor=#000000;"
              "fontColor=#000000;fontStyle=1;fontSize=10;")
S_ALT      = ("rounded=1;whiteSpace=wrap;html=1;"
              "fillColor=#EEEEEE;strokeColor=#000000;"
              "fontColor=#000000;fontStyle=0;fontSize=10;dashed=1;")
S_DOC      = ("shape=document;whiteSpace=wrap;html=1;"
              "fillColor=#EEEEEE;strokeColor=#000000;"
              "fontColor=#000000;fontStyle=0;fontSize=10;")
S_HEADER   = ("rounded=1;whiteSpace=wrap;html=1;"
              "fillColor=#000000;strokeColor=#000000;"
              "fontColor=#FFFFFF;fontStyle=1;fontSize=13;"
              "align=center;verticalAlign=middle;")
S_SECTION  = ("rounded=1;whiteSpace=wrap;html=1;"
              "fillColor=#DDDDDD;strokeColor=#000000;"
              "fontColor=#000000;fontStyle=1;fontSize=11;align=center;")
S_LEG_BG   = ("rounded=1;fillColor=#FFFFFF;strokeColor=#000000;")
S_FIRMA_BG = ("rounded=0;fillColor=#FFFFFF;strokeColor=#000000;")
S_TEXT_B   = "text;html=1;fontSize=11;fontColor=#000000;align=center;fontStyle=1;"
S_TEXT_C   = "text;html=1;fontSize=10;fontColor=#000000;align=center;"
S_TEXT_L   = "text;html=1;fontSize=9;fontColor=#000000;align=left;verticalAlign=middle;"
S_ARROW    = "edgeStyle=orthogonalEdgeStyle;html=1;fontSize=10;fontColor=#000000;"
S_ARROW_D  = "edgeStyle=orthogonalEdgeStyle;dashed=1;html=1;fontSize=10;fontColor=#000000;"

def cell(cid, value, style, x, y, w, h):
    geo = f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
    return (f'<mxCell id="{cid}" value="{value}" style="{style}" '
            f'vertex="1" parent="1">{geo}</mxCell>\n')

def edge(cid, label, style, src, tgt):
    return (f'<mxCell id="{cid}" value="{label}" style="{style}" '
            f'edge="1" source="{src}" target="{tgt}" parent="1">'
            f'<mxGeometry relative="1" as="geometry"/></mxCell>\n')
def leyenda(pfx, LX, LY):
    c = []
    # Ancho 175, alto 210  (compacto)
    LW, LH = 175, 215
    c.append(cell(f"{pfx}_leg_bg", "", S_LEG_BG, LX, LY, LW, LH))
    c.append(cell(f"{pfx}_leg_tit", "Simbología",
                  S_TEXT_B, LX, LY+6, LW, 20))

    items = [
        ("lt1", "",  S_TERMINAL, 44, 26),
        ("lt2", "",  S_PROCESS,  70, 24),
        ("lt3", "",  S_DECISION, 44, 28),
        ("lt4", "",  S_ALT,      70, 24),
        ("lt5", "",  S_DOC,      70, 24),
    ]
    labels = ["Inicio / Fin", "Proceso", "Decisión",
              "Rama alterna", "Documento"]
    row_h = 36
    for i, (lid, val, sty, sw, sh) in enumerate(items):
        ry = LY + 32 + i * row_h
        sx = LX + 8
        c.append(cell(f"{pfx}_{lid}",   val, sty,     sx,            ry,           sw, sh))
        c.append(cell(f"{pfx}_{lid}t",  labels[i], S_TEXT_L,
                      sx + sw + 8,  ry + (sh-18)//2, LW-sw-20, 18))
    return "".join(c)


# ─────────────────────────────────────────────────────────
#  SECCIÓN DE AUTORIZACIÓN — reutilizable
#  x0=inicio izq, YA=y top, total_w=ancho total
# ─────────────────────────────────────────────────────────
def autorizacion(pfx, x0, YA, total_w):
    c = []
    c.append(cell(f"{pfx}_auth_sec", "AUTORIZACIÓN",
                  S_SECTION, x0, YA, total_w, 32))
    fw = total_w // 4
    fh = 80
    for i, lbl in enumerate(["Elaboró:", "Revisó:", "Validó:", "Fecha:"]):
        fx = x0 + i * fw
        c.append(cell(f"{pfx}_fb{i}", "",  S_FIRMA_BG, fx,   YA+32, fw, fh))
        c.append(cell(f"{pfx}_fl{i}", lbl, S_TEXT_B,   fx+5, YA+37, fw-10, 18))
    return "".join(c)



# ═════════════════════════════════════════════════════════
#  TAP-01 · Higiene de manos — programa terapia asistida
# ═════════════════════════════════════════════════════════
def diagram_tap01():
    c = []
    CX, CW = 200, 340
    CC = CX + CW // 2
    AX, AW = 580, 250
    LX = 830

    c.append(cell("h",
        "TAP-01 · Higiene de manos — Terapia asistida con perros&#xa;"
        "Hospital de Salud Mental Orizaba · MOCEBPASS",
        S_HEADER, 30, 20, 760, 75))

    YI=135; Y1=215; Y2=320; Y3=425; Y4=570; Y5=675
    Y6=780; Y7=930; Y8=1050; Y9=1175

    c.append(cell("ini",  "INICIO",   S_TERMINAL, CC-70, YI,   140, 50))
    c.append(cell("n1",   "Llegada a la unidad&#xa;(personal del programa TAP)",
                  S_PROCESS, CX, Y1, CW, 60))
    c.append(cell("n2",   "Higiene de manos — Momento 1&#xa;(antes del contacto con el paciente)",
                  S_PROCESS, CX, Y2, CW, 60))
    c.append(cell("d1",   "¿Manos con lesiones, uñas largas&#xa;o esmalte?",
                  S_DECISION, CX, Y3, CW, 85))
    c.append(cell("alt1", "Colocarse guantes o quedar&#xa;excluido temporal de la sesión&#xa;(enfermería)",
                  S_ALT, AX, Y3+5, AW, 75))
    c.append(cell("n3",   "Higiene de manos antes del contacto&#xa;con el perro y su cuidador (enfermería)",
                  S_PROCESS, CX, Y4, CW, 60))
    c.append(cell("n4",   "Sesión TAP: higiene entre pacientes&#xa;y tras contacto con el perro&#xa;(momentos 2-3)&#xa;(personal de sesión)",
                  S_PROCESS, CX, Y5, CW, 85))
    c.append(cell("n5",   "Higiene con agua y jabón (momento 4)&#xa;y lavado de materiales del perro&#xa;(personal de sesión)",
                  S_PROCESS, CX, Y6, CW, 85))
    c.append(cell("d2",   "¿Incidencia o omisión&#xa;detectada en los momentos críticos?",
                  S_DECISION, CX, Y7, CW, 85))
    c.append(cell("alt2", "Reportar al comité de infecciones&#xa;nosocomiales y registrar la incidencia&#xa;(coordinador del programa)",
                  S_ALT, AX, Y7+5, AW, 75))
    c.append(cell("n6",   "Higiene antes de abandonar el área&#xa;y de manipular el expediente (momento 5)&#xa;(todo el personal)",
                  S_PROCESS, CX, Y8, CW, 60))
    c.append(cell("doc",  "Bitácora de higiene&#xa;de manos del programa",
                  S_DOC, 15, Y8+30, 130, 55))
    c.append(cell("fin",  "FIN",     S_TERMINAL, CC-70, Y9,   140, 50))

    c.append(edge("e1", "",  S_ARROW, "ini", "n1"))
    c.append(edge("e2", "",  S_ARROW, "n1",  "n2"))
    c.append(edge("e3", "",  S_ARROW, "n2",  "d1"))
    c.append(edge("e4", "SÍ", S_ARROW, "d1", "alt1"))
    c.append(edge("e5", "NO", S_ARROW, "d1", "n3"))
    c.append(edge("e6", "",  S_ARROW, "alt1", "n3"))
    c.append(edge("e7", "",  S_ARROW, "n3",  "n4"))
    c.append(edge("e8", "",  S_ARROW, "n4",  "n5"))
    c.append(edge("e8b", "", S_ARROW, "n5",  "d2"))
    c.append(edge("e9", "SÍ", S_ARROW, "d2", "alt2"))
    c.append(edge("e10","NO", S_ARROW, "d2", "n6"))
    c.append(edge("e11","",  S_ARROW, "alt2", "n6"))
    c.append(edge("e12","",  S_ARROW, "n6",  "doc"))
    c.append(edge("e13","",  S_ARROW, "n6",  "fin"))
    c.append(leyenda("tap01", LX, 135))
    c.append(autorizacion("tap01", 30, Y9+80, 760))
    return "".join(c)


# ═════════════════════════════════════════════════════════
#  TAP-02 · Miasis gusano barrenador caninos/felinos
# ═════════════════════════════════════════════════════════
def diagram_tap02():
    c = []
    CX, CW = 200, 340
    CC = CX + CW // 2
    AX, AW = 580, 250
    LX = 830

    c.append(cell("h",
        "TAP-02 · Miasis por gusano barrenador — Caninos y felinos&#xa;"
        "Hospital de Salud Mental Orizaba · MOCEBPASS",
        S_HEADER, 30, 20, 760, 75))

    YI=135; Y1=215; Y2=320; Y3=425; Y4=570; Y5=675
    Y6=780; Y7=930; Y8=1050; Y9=1175; Y10=1300

    c.append(cell("ini",  "INICIO",   S_TERMINAL, CC-70, YI,   140, 50))
    c.append(cell("n1",   "Inspección corporal del animal&#xa;antes de cada sesión&#xa;(cuidador canino)",
                  S_PROCESS, CX, Y1, CW, 60))
    c.append(cell("d1",   "¿Sospecha de miiasis?&#xa;(larvas u orificios&#xa;respiratorios)",
                  S_DECISION, CX, Y2, CW, 85))
    c.append(cell("alt1", "Suspensión inmediata de sesiones&#xa;y aislamiento zoosanitario&#xa;(cuidador canino)",
                  S_ALT, AX, Y2+5, AW, 75))
    c.append(cell("n2",   "Manejo veterinario: remoción de larvas,&#xa;antiséptico, ivermectina, antibiótico&#xa;(veterinario del programa)",
                  S_PROCESS, CX, Y3, CW, 85))
    c.append(cell("d2",   "¿Confirmado como&#xa;C. hominivorax?",
                  S_DECISION, CX, Y4, CW, 85))
    c.append(cell("alt2", "Notificación inmediata a&#xa;SENASICA/CNMVB en ≤ 24 h&#xa;(veterinario del programa)",
                  S_ALT, AX, Y4+5, AW, 75))
    c.append(cell("n3",   "Desparasitación y vacunación vigente;&#xa;prevención ambiental&#xa;(cuidador canino)",
                  S_PROCESS, CX, Y5, CW, 60))
    c.append(cell("d3",   "¿Cicatrizado y con liberación&#xa;veterinaria por escrito?",
                  S_DECISION, CX, Y6, CW, 85))
    c.append(cell("alt3", "Permanece suspendido del programa&#xa;hasta cumplir apto zoosanitario&#xa;(cuidador canino)",
                  S_ALT, AX, Y6+5, AW, 75))
    c.append(cell("n7",   "Reincorporación al programa&#xa;(cuidador canino)",
                  S_PROCESS, CX, Y7, CW, 60))
    c.append(cell("doc",  "Bitácora zoosanitaria&#xa;y cartilla del animal",
                  S_DOC, 15, Y7+30, 130, 55))
    c.append(cell("fin",  "FIN",     S_TERMINAL, CC-70, Y8+120, 140, 50))

    c.append(edge("e1", "",  S_ARROW, "ini", "n1"))
    c.append(edge("e2", "",  S_ARROW, "n1",  "d1"))
    c.append(edge("e3", "SÍ", S_ARROW, "d1", "alt1"))
    c.append(edge("e4", "",  S_ARROW, "alt1", "n2"))
    c.append(edge("e5", "NO", S_ARROW, "d1", "n3"))
    c.append(edge("e6", "",  S_ARROW, "n2",  "d2"))
    c.append(edge("e7", "SÍ", S_ARROW, "d2", "alt2"))
    c.append(edge("e8", "",  S_ARROW, "alt2", "n3"))
    c.append(edge("e9", "NO", S_ARROW, "d2", "n3"))
    c.append(edge("e10","",  S_ARROW, "n3",  "d3"))
    c.append(edge("e11","SÍ", S_ARROW, "d3", "n7"))
    c.append(edge("e12","NO", S_ARROW, "d3", "alt3"))
    c.append(edge("e13","",  S_ARROW, "alt3", "n3"))
    c.append(edge("e14","",  S_ARROW, "n7",  "doc"))
    c.append(edge("e15","",  S_ARROW, "n7",  "fin"))
    c.append(leyenda("tap02", LX, 135))
    c.append(autorizacion("tap02", 30, Y8+230, 760))
    return "".join(c)


# ═════════════════════════════════════════════════════════
#  TAP-03 · Miasis por gusano barrenador en humanos
# ═════════════════════════════════════════════════════════
def diagram_tap03():
    c = []
    CX, CW = 200, 340
    CC = CX + CW // 2
    AX, AW = 580, 250
    LX = 830

    c.append(cell("h",
        "TAP-03 · Miasis por gusano barrenador — Pacientes humanos&#xa;"
        "Hospital de Salud Mental Orizaba · MOCEBPASS",
        S_HEADER, 30, 20, 760, 75))

    YI=135; Y1=215; Y2=320; Y3=425; Y4=570; Y5=675
    Y6=780; Y7=930; Y8=1050; Y9=1175; Y10=1300

    c.append(cell("ini",  "INICIO",   S_TERMINAL, CC-70, YI,   140, 50))
    c.append(cell("n1",   "Paciente con lesión sospechosa&#xa;de miiasis&#xa;(urgencias / hospitalización)",
                  S_PROCESS, CX, Y1, CW, 60))
    c.append(cell("n2",   "Exploración: orificios, profundidad,&#xa;extensión, estado general&#xa;(médico adscrito)",
                  S_PROCESS, CX, Y2, CW, 60))
    c.append(cell("d1",   "¿Confirmación de larvas&#xa;de C. hominivorax?",
                  S_DECISION, CX, Y3, CW, 85))
    c.append(cell("alt1", "Manejo de otra etiología;&#xa;referencia o diagnóstico alternativo&#xa;(médico adscrito)",
                  S_ALT, AX, Y3+5, AW, 75))
    c.append(cell("n3",   "Remoción: vaselina 5-10 min,&#xa;extracción con pinzas sin romper larva&#xa;(médico adscrito)",
                  S_PROCESS, CX, Y4, CW, 85))
    c.append(cell("n4",   "Limpieza y desbridamiento;&#xa;curación con vigilancia diaria&#xa;(médico y enfermería)",
                  S_PROCESS, CX, Y5, CW, 60))
    c.append(cell("n5",   "Tratamiento: ivermectina oral según severidad,&#xa;antibiótico si hay sobreinfección, analgesia,&#xa;profilaxis antitetánica (médico adscrito)",
                  S_PROCESS, CX, Y6, CW, 85))
    c.append(cell("n6",   "Notificación a epidemiología&#xa;hospitalaria (SISVEP)&#xa;(médico adscrito)",
                  S_PROCESS, CX, Y7, CW, 60))
    c.append(cell("n8",   "Estudio del entorno y control vectorial&#xa;(enfermería y epidemiología)",
                  S_PROCESS, CX, Y8-10, CW, 60))
    c.append(cell("doc",  "Expediente clínico&#xa;+ notificación SISVEP",
                  S_DOC, 15, Y8+30, 130, 55))
    c.append(cell("fin",  "FIN",     S_TERMINAL, CC-70, Y9,   140, 50))

    c.append(edge("e1", "",  S_ARROW, "ini", "n1"))
    c.append(edge("e2", "",  S_ARROW, "n1",  "n2"))
    c.append(edge("e3", "",  S_ARROW, "n2",  "d1"))
    c.append(edge("e4", "NO", S_ARROW, "d1", "alt1"))
    c.append(edge("e5", "",  S_ARROW, "alt1", "n3"))
    c.append(edge("e6", "SÍ", S_ARROW, "d1", "n3"))
    c.append(edge("e7", "",  S_ARROW, "n3",  "n4"))
    c.append(edge("e8", "",  S_ARROW, "n4",  "n5"))
    c.append(edge("e9", "",  S_ARROW, "n5",  "n6"))
    c.append(edge("e10","",  S_ARROW, "n6",  "doc"))
    c.append(edge("e11","",  S_ARROW, "n6",  "n8"))
    c.append(edge("e12","",  S_ARROW, "n8",  "fin"))
    c.append(leyenda("tap03", LX, 135))
    c.append(autorizacion("tap03", 30, Y9+80, 760))
    return "".join(c)

DIAGRAMAS_TAP = {
    "TAP-01": diagram_tap01,
    "TAP-02": diagram_tap02,
    "TAP-03": diagram_tap03,
}

def construir_drawio_tap():
    """Construye el .drawio de los 3 procesos TAP en un archivo propio (3 pestañas)."""
    tablas = []
    for clave in ("TAP-01", "TAP-02", "TAP-03"):
        celdas = DIAGRAMAS_TAP[clave]()
        tablas.append((clave, celdas))
    pages = []
    for nombre, celdas in tablas:
        pages.append(f'    <diagram id="{nombre.lower().replace("-", "")}" name="{nombre}">\n'
                     f'      <mxGraphModel dx="800" dy="600" grid="1" gridSize="10" guides="1" '
                     f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
                     f'pageWidth="1100" pageHeight="1700" math="0" shadow="0">\n'
                     f'        <root>\n'
                     f'          <mxCell id="0"/>\n'
                     f'          <mxCell id="1" parent="0"/>\n'
                     + celdas +
                     '        </root>\n'
                     '      </mxGraphModel>\n'
                     '    </diagram>\n')
    xml = ('<mxfile host="app.diagrams.net" modified="2026-09-07T00:00:00.000Z" '
           'agent="gen_drawio_tap" version="21.0.0" type="device">\n'
           + "".join(pages) + '</mxfile>\n')
    return xml

if __name__ == '__main__':
    import sys
    salida = sys.argv[1] if len(sys.argv) > 1 else 'EjeTAP_Algoritmos_MOCEBPASS.drawio'
    xml = construir_drawio_tap()
    open(salida, 'w', encoding='utf-8').write(xml)
    print('drawio escrito:', salida)
    # validar XML
    import xml.etree.ElementTree as ET
    ET.parse(salida)
    print('XML válido OK')
