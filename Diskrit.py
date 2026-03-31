import streamlit as st
import requests
import time
from sympy.logic.boolalg import *
import sympy as sp

st.set_page_config(layout="wide")
if 'kondisi' not in st.session_state:
    st.session_state['kondisi'] = {"kover":True,"pertemuan1":False, "pertemuan2":False,
                                   "pertemuan3":False,"pertemuan4":False}
st.title("Matematika Diskrit")

#------------------------------------

st.markdown('''
            <style>
            #pert1{
                font-family:broadway;
                font-size: 30px;
                color:yellow;
                text-shadow:2px 2px  red, -2px -2px  blue;
            }
            .konsep1{
                font-family: "Times New Roman";
                font-size:20px;
            }
            tr{
                text-align:center;
            }
            td {
              border: 2px solid;
              font-family:"courier new";
              font-size:20px;
            }
            th{
                font-family:"Times new roman";
                font-size:30px;
                text-align:center;
                background-color:yellow;
                color:green;
                
            }
            </style>
            ''',unsafe_allow_html=True)

#-------------------------------------
def pendahuluan():
    menu2 = st.tabs(['Pendahuluan','Perpustakaan'])
    if menu2[0]:
        tulisanHTML = '''
    <!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Silabus Matematika Diskrit</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=JetBrains+Mono:wght@300;400;500&family=Crimson+Pro:ital,wght@0,300;0,400;0,600;1,300;1,400&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<style>
  :root {
    --ink: #0f0e0c;
    --paper: #f5f0e8;
    --cream: #ede8db;
    --gold: #b8943f;
    --gold-light: #d4af6a;
    --red: #8b2635;
    --blue: #1a3a5c;
    --muted: #6b6355;
    --line: #c8bfa8;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--paper);
    color: var(--ink);
    font-family: 'Crimson Pro', Georgia, serif;
    font-size: 17px;
    line-height: 1.7;
    min-height: 100vh;
  }

  /* Noise texture overlay */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.4;
  }

  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 2rem 4rem;
    position: relative;
    z-index: 1;
  }

  /* ── HEADER ── */
  header {
    padding: 3.5rem 0 2rem;
    border-bottom: 2px solid var(--ink);
    position: relative;
  }

  .header-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.8rem;
  }

  h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.4rem, 6vw, 4rem);
    font-weight: 900;
    line-height: 1.05;
    color: var(--ink);
    letter-spacing: -0.01em;
  }

  h1 em {
    font-style: italic;
    color: var(--red);
  }

  .header-sub {
    margin-top: 1rem;
    font-size: 1.05rem;
    color: var(--muted);
    font-style: italic;
    max-width: 540px;
  }

  .header-stats {
    display: flex;
    gap: 2.5rem;
    margin-top: 1.8rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--line);
  }

  .stat {
    display: flex;
    flex-direction: column;
  }

  .stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--blue);
    line-height: 1;
  }

  .stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 0.2rem;
  }

  /* ── FILTER BAR ── */
  .filter-bar {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    padding: 1.5rem 0;
    border-bottom: 1px solid var(--line);
  }

  .filter-btn {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.35rem 0.9rem;
    border: 1px solid var(--line);
    background: transparent;
    color: var(--muted);
    cursor: pointer;
    transition: all 0.2s;
    border-radius: 2px;
  }

  .filter-btn:hover, .filter-btn.active {
    background: var(--ink);
    color: var(--paper);
    border-color: var(--ink);
  }

  /* ── MODULE ── */
  .module {
    margin-top: 3rem;
  }

  .module-header {
    display: flex;
    align-items: baseline;
    gap: 1.2rem;
    margin-bottom: 1.2rem;
  }

  .module-num {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 900;
    color: var(--cream);
    line-height: 1;
    -webkit-text-stroke: 1.5px var(--line);
    flex-shrink: 0;
  }

  .module-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.45rem;
    font-weight: 700;
    color: var(--blue);
    line-height: 1.2;
  }

  .module-title span {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 400;
    margin-bottom: 0.2rem;
  }

  /* ── PERTEMUAN CARD ── */
  .sessions {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-left: 2px solid var(--line);
    margin-left: 1.2rem;
    padding-left: 0;
  }

  .session {
    display: grid;
    grid-template-columns: 80px 1fr;
    border-bottom: 1px solid var(--line);
    transition: background 0.2s;
    cursor: pointer;
    position: relative;
  }

  .session:last-child { border-bottom: none; }

  .session::before {
    content: '';
    position: absolute;
    left: -8px;
    top: 50%;
    transform: translateY(-50%);
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--paper);
    border: 2px solid var(--line);
    transition: all 0.2s;
  }

  .session:hover::before, .session.expanded::before {
    background: var(--gold);
    border-color: var(--gold);
  }

  .session:hover { background: rgba(184,148,63,0.05); }
  .session.special { background: rgba(26,58,92,0.04); }
  .session.special:hover { background: rgba(26,58,92,0.08); }

  .session-num {
    padding: 1.2rem 1rem 1.2rem 1.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--muted);
    letter-spacing: 0.08em;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.2rem;
  }

  .session-num strong {
    font-size: 1.3rem;
    font-weight: 500;
    color: var(--ink);
    font-family: 'Playfair Display', serif;
  }

  .session-body {
    padding: 1.2rem 1.5rem 1.2rem 0.5rem;
  }

  .session-title {
    font-family: 'Crimson Pro', serif;
    font-size: 1.08rem;
    font-weight: 600;
    color: var(--ink);
    line-height: 1.35;
    margin-bottom: 0.3rem;
  }

  .session-focus {
    font-size: 0.88rem;
    color: var(--muted);
    font-style: italic;
    line-height: 1.4;
  }

  .session-detail {
    display: none;
    margin-top: 1rem;
    padding: 1rem 1.2rem;
    background: var(--cream);
    border-radius: 3px;
    border-left: 3px solid var(--gold);
  }

  .session.expanded .session-detail { display: block; }

  .session-detail h4 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.6rem;
  }

  .session-detail ul {
    list-style: none;
    padding: 0;
  }

  .session-detail ul li {
    font-size: 0.9rem;
    color: var(--ink);
    padding: 0.2rem 0;
    padding-left: 1.2rem;
    position: relative;
  }

  .session-detail ul li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--gold);
    font-size: 0.8rem;
  }

  .badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.15rem 0.5rem;
    border-radius: 2px;
    margin-left: 0.4rem;
    vertical-align: middle;
  }

  .badge-exam {
    background: var(--blue);
    color: white;
  }

  .badge-proof {
    background: var(--red);
    color: white;
  }

  /* ── LEGEND ── */
  .legend {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    margin-top: 3rem;
    padding: 1.2rem 1.5rem;
    background: var(--cream);
    border: 1px solid var(--line);
    border-radius: 3px;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.82rem;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.06em;
  }

  .legend-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  /* ── FOOTER ── */
  footer {
    margin-top: 4rem;
    padding-top: 1.5rem;
    border-top: 2px solid var(--ink);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ── PROGRESS ── */
  .progress-track {
    display: flex;
    gap: 3px;
    margin-top: 1.5rem;
    flex-wrap: wrap;
  }

  .progress-pip {
    width: calc((100% - 45px) / 16);
    height: 6px;
    border-radius: 1px;
    background: var(--line);
    transition: background 0.3s;
    cursor: pointer;
    position: relative;
  }

  .progress-pip.active { background: var(--gold); }
  .progress-pip.exam { background: var(--blue); }
  .progress-pip:hover::after {
    content: attr(data-label);
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--ink);
    color: var(--paper);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    white-space: nowrap;
    padding: 0.2rem 0.5rem;
    border-radius: 2px;
    pointer-events: none;
    z-index: 10;
  }

  /* Animations */
  .module { opacity: 0; transform: translateY(20px); animation: fadeUp 0.5s forwards; }
  .module:nth-child(1) { animation-delay: 0.1s; }
  .module:nth-child(2) { animation-delay: 0.2s; }
  .module:nth-child(3) { animation-delay: 0.3s; }
  .module:nth-child(4) { animation-delay: 0.4s; }

  @keyframes fadeUp {
    to { opacity: 1; transform: none; }
  }

  .hidden { display: none !important; }

  @media (max-width: 600px) {
    .session { grid-template-columns: 60px 1fr; }
    .header-stats { gap: 1.5rem; }
    .stat-num { font-size: 1.5rem; }
  }
</style>
</head>
<body>
<div class="container">

  <header>
    <div class="header-meta">Silabus Mata Kuliah &nbsp;·&nbsp; Semester Ganjil</div>
    <h1>Matematika<br><em>Diskrit</em></h1>
    <p class="header-sub">Fokus pada topik fundamental dan teknik pembuktian dalam matematika diskrit untuk ilmu komputer.</p>

    <div class="header-stats">
      <div class="stat"><span class="stat-num">16</span><span class="stat-label">Pertemuan</span></div>
      <div class="stat"><span class="stat-num">4</span><span class="stat-label">Modul</span></div>
      <div class="stat"><span class="stat-num">12</span><span class="stat-label">Topik Materi</span></div>
      <div class="stat"><span class="stat-num">2</span><span class="stat-label">Ujian</span></div>
    </div>

    <div class="progress-track" id="progressTrack"></div>
  </header>

  <div class="filter-bar">
    <button class="filter-btn active" data-filter="all">Semua</button>
    <button class="filter-btn" data-filter="logika">Logika</button>
    <button class="filter-btn" data-filter="himpunan">Himpunan & Relasi</button>
    <button class="filter-btn" data-filter="induksi">Induksi & Rekurensi</button>
    <button class="filter-btn" data-filter="kombinatorika">Kombinatorika & Graf</button>
    <button class="filter-btn" data-filter="ujian">Ujian</button>
  </div>

  <div id="syllabus">

    <!-- MODULE 1 -->
    <div class="module" data-module="1">
      <div class="module-header">
        <div class="module-num">01</div>
        <div class="module-title">
          <span>Modul Pertama</span>
          Logika dan Dasar Pembuktian
        </div>
      </div>
      <div class="sessions">

        <div class="session" data-session="1" data-tag="logika">
          <div class="session-num"><span>Prt.</span><strong>01</strong></div>
          <div class="session-body">
            <div class="session-title">Logika Proposisi & Ekuivalensi Logis <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Pembuktian dengan Tabel Kebenaran dan Hukum Logika</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Proposisi, konjungsi, disjungsi, negasi, implikasi, biimplikasi</li>
                <li>Tabel kebenaran untuk ekspresi majemuk</li>
                <li>Hukum De Morgan, hukum distribusi, hukum absorpsi</li>
                <li>Membuktikan ekuivalensi logis: \(p \leftrightarrow q \equiv (p \to q) \land (q \to p)\)</li>
                <li>Tautologi dan kontradiksi</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="2" data-tag="logika">
          <div class="session-num"><span>Prt.</span><strong>02</strong></div>
          <div class="session-body">
            <div class="session-title">Kuantor \(\forall, \exists\) dan Validitas Argumen <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Negasi kuantor, Modus Ponens, Modus Tollens, Silogisme</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Kuantor universal \(\forall\) dan eksistensial \(\exists\)</li>
                <li>Negasi: \(\neg\forall x\,P(x) \equiv \exists x\,\neg P(x)\)</li>
                <li>Modus Ponens: \(p, p \to q \vdash q\)</li>
                <li>Modus Tollens: \(\neg q, p \to q \vdash \neg p\)</li>
                <li>Silogisme Hipotetis dan Disjungtif</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="3" data-tag="logika">
          <div class="session-num"><span>Prt.</span><strong>03</strong></div>
          <div class="session-body">
            <div class="session-title">Pembuktian Langsung & Kontrapositif <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Direct Proof dan Indirect Proof (Contrapositive)</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Struktur pembuktian langsung: asumsikan \(p\), tunjukkan \(q\)</li>
                <li>Contoh: Buktikan "jika \(n\) ganjil maka \(n^2\) ganjil"</li>
                <li>Pembuktian kontrapositif: buktikan \(\neg q \to \neg p\)</li>
                <li>Kapan memilih metode pembuktian yang tepat</li>
                <li>Latihan pembuktian bilangan genap/ganjil</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="4" data-tag="logika">
          <div class="session-num"><span>Prt.</span><strong>04</strong></div>
          <div class="session-body">
            <div class="session-title">Pembuktian dengan Kontradiksi <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Reductio ad Absurdum</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Struktur: asumsikan \(\neg p\), derivasikan kontradiksi</li>
                <li>Bukti klasik: \(\sqrt{2}\) adalah bilangan irasional</li>
                <li>Bukti infinitas bilangan prima</li>
                <li>Perbedaan proof by contradiction vs contrapositive</li>
                <li>Pembuktian eksistensi dengan kontradiksi</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- MODULE 2 -->
    <div class="module" data-module="2">
      <div class="module-header">
        <div class="module-num">02</div>
        <div class="module-title">
          <span>Modul Kedua</span>
          Teori Himpunan dan Relasi
        </div>
      </div>
      <div class="sessions">

        <div class="session" data-session="5" data-tag="himpunan">
          <div class="session-num"><span>Prt.</span><strong>05</strong></div>
          <div class="session-body">
            <div class="session-title">Pembuktian Kesamaan Himpunan <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">\(A = B \iff A \subseteq B \land B \subseteq A\)</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Operasi himpunan: irisan, gabungan, komplemen, selisih</li>
                <li>Teknik pembuktian subset ganda (double containment)</li>
                <li>Pembuktian \(A \cup (B \cap C) = (A \cup B) \cap (A \cup C)\)</li>
                <li>Hukum De Morgan untuk himpunan</li>
                <li>Diagram Venn sebagai alat bantu intuisi</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="6" data-tag="himpunan">
          <div class="session-num"><span>Prt.</span><strong>06</strong></div>
          <div class="session-body">
            <div class="session-title">Relasi Ekivalen dan Partisi <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Membuktikan sifat Refleksif, Simetris, dan Transitif</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Definisi relasi dan representasi matriks/graf</li>
                <li>Sifat refleksif: \(\forall a, (a,a) \in R\)</li>
                <li>Sifat simetris: \((a,b) \in R \Rightarrow (b,a) \in R\)</li>
                <li>Sifat transitif: \((a,b),(b,c) \in R \Rightarrow (a,c) \in R\)</li>
                <li>Kelas ekivalen dan teorema partisi</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="7" data-tag="himpunan">
          <div class="session-num"><span>Prt.</span><strong>07</strong></div>
          <div class="session-body">
            <div class="session-title">Fungsi Injektif, Surjektif, dan Bijektif <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Pembuktian komposisi fungsi bijektif</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Definisi fungsi: domain, kodomain, range</li>
                <li>Injektif (satu-satu): \(f(a)=f(b) \Rightarrow a=b\)</li>
                <li>Surjektif (onto): \(\forall b \in B, \exists a: f(a)=b\)</li>
                <li>Bijektif = injektif + surjektif</li>
                <li>Teorema: jika \(f,g\) bijektif maka \(g \circ f\) bijektif</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session special" data-session="8" data-tag="ujian">
          <div class="session-num"><span>Prt.</span><strong>08</strong></div>
          <div class="session-body">
            <div class="session-title">UTS — Ujian Tengah Semester <span class="badge badge-exam">Exam</span></div>
            <div class="session-focus">Modul 1 & 2 · Logika, Pembuktian, Himpunan, Relasi, Fungsi</div>
            <div class="session-detail">
              <h4>Cakupan Materi</h4>
              <ul>
                <li>Logika proposisi dan ekuivalensi logis</li>
                <li>Metode pembuktian: langsung, kontrapositif, kontradiksi</li>
                <li>Teori himpunan dan operasinya</li>
                <li>Relasi ekivalen dan partisi</li>
                <li>Fungsi injektif, surjektif, bijektif</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- MODULE 3 -->
    <div class="module" data-module="3">
      <div class="module-header">
        <div class="module-num">03</div>
        <div class="module-title">
          <span>Modul Ketiga</span>
          Induksi Matematika & Rekurensi
        </div>
      </div>
      <div class="sessions">

        <div class="session" data-session="9" data-tag="induksi">
          <div class="session-num"><span>Prt.</span><strong>09</strong></div>
          <div class="session-body">
            <div class="session-title">Induksi Matematika Lemah <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Langkah Basis dan Langkah Induksi</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Prinsip induksi matematika: basis + langkah induktif</li>
                <li>Contoh: \(\sum_{i=1}^{n} i = \frac{n(n+1)}{2}\)</li>
                <li>Induksi pada ketidaksetaraan: \(2^n > n\) untuk \(n \geq 1\)</li>
                <li>Kesalahan umum dalam pembuktian induksi</li>
                <li>Variasi: induksi mundur</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="10" data-tag="induksi">
          <div class="session-num"><span>Prt.</span><strong>10</strong></div>
          <div class="session-body">
            <div class="session-title">Induksi Kuat & Well-Ordering Principle <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Prinsip Induksi Kuat dan Prinsip Sumur</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Perbedaan induksi lemah dan kuat</li>
                <li>Induksi kuat: asumsikan \(P(1), P(2), \ldots, P(k)\) untuk membuktikan \(P(k+1)\)</li>
                <li>Well-Ordering Principle: setiap himpunan non-kosong bilangan asli punya elemen terkecil</li>
                <li>Ekuivalensi ketiga prinsip</li>
                <li>Aplikasi: pembuktian faktorisasi prima unik</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="11" data-tag="induksi">
          <div class="session-num"><span>Prt.</span><strong>11</strong></div>
          <div class="session-body">
            <div class="session-title">Relasi Rekurensi Homogen Linear <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Rumus eksplisit Barisan Fibonacci dan rekurensi linear</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Definisi relasi rekurensi dan solusi closed-form</li>
                <li>Persamaan karakteristik relasi rekurensi orde-2</li>
                <li>Barisan Fibonacci: \(F_n = F_{n-1} + F_{n-2}\)</li>
                <li>Formula Binet: \(F_n = \frac{\phi^n - \psi^n}{\sqrt{5}}\)</li>
                <li>Verifikasi dengan induksi matematika</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- MODULE 4 -->
    <div class="module" data-module="4">
      <div class="module-header">
        <div class="module-num">04</div>
        <div class="module-title">
          <span>Modul Keempat</span>
          Kombinatorika dan Graf
        </div>
      </div>
      <div class="sessions">

        <div class="session" data-session="12" data-tag="kombinatorika">
          <div class="session-num"><span>Prt.</span><strong>12</strong></div>
          <div class="session-body">
            <div class="session-title">Inklusi-Eksklusi & Pigeonhole Principle <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Pembuktian Eksistensi</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Prinsip Inklusi-Eksklusi: \(|A \cup B| = |A| + |B| - |A \cap B|\)</li>
                <li>Generalisasi untuk \(n\) himpunan</li>
                <li>Pigeonhole Principle: \(n+1\) objek ke \(n\) kotak → ∃ kotak ≥ 2 objek</li>
                <li>Pigeonhole umum: \(\lceil m/n \rceil\)</li>
                <li>Aplikasi: pembuktian eksistensi tanpa konstruksi eksplisit</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="13" data-tag="kombinatorika">
          <div class="session-num"><span>Prt.</span><strong>13</strong></div>
          <div class="session-body">
            <div class="session-title">Pengantar Teori Graf & Handshaking Lemma <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Jumlah derajat simpul \(= 2 \times\) jumlah sisi</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Definisi graf: simpul (vertex), sisi (edge), derajat</li>
                <li>Graf berarah dan tidak berarah</li>
                <li>Handshaking Lemma: \(\sum_{v \in V} \deg(v) = 2|E|\)</li>
                <li>Korolari: jumlah simpul berderajat ganjil selalu genap</li>
                <li>Representasi graf: matriks ketetanggaan, daftar ketetanggaan</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="14" data-tag="kombinatorika">
          <div class="session-num"><span>Prt.</span><strong>14</strong></div>
          <div class="session-body">
            <div class="session-title">Graf Euler dan Hamilton <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Syarat perlu dan cukup keberadaan lintasan</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Lintasan dan sirkuit Euler</li>
                <li>Teorema Euler: graf terhubung memiliki sirkuit Euler \(\iff\) semua simpul berderajat genap</li>
                <li>Algoritma Hierholzer</li>
                <li>Lintasan dan sirkuit Hamilton (NP-complete)</li>
                <li>Kondisi cukup: Teorema Dirac dan Ore</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session" data-session="15" data-tag="kombinatorika">
          <div class="session-num"><span>Prt.</span><strong>15</strong></div>
          <div class="session-body">
            <div class="session-title">Pohon (Trees) & Propertinya <span class="badge badge-proof">Proof</span></div>
            <div class="session-focus">Graf terhubung dengan \(n\) simpul dan \(n-1\) sisi adalah pohon</div>
            <div class="session-detail">
              <h4>Topik yang Dibahas</h4>
              <ul>
                <li>Definisi pohon: graf terhubung tanpa siklus</li>
                <li>Ekuivalensi: 5 karakterisasi pohon</li>
                <li>Pembuktian: pohon dengan \(n\) simpul punya tepat \(n-1\) sisi</li>
                <li>Pohon rentang (spanning tree) dan algoritma Kruskal</li>
                <li>Pohon berakar dan representasinya</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="session special" data-session="16" data-tag="ujian">
          <div class="session-num"><span>Prt.</span><strong>16</strong></div>
          <div class="session-body">
            <div class="session-title">UAS — Ujian Akhir Semester <span class="badge badge-exam">Exam</span></div>
            <div class="session-focus">Modul 3 & 4 · Induksi, Rekurensi, Kombinatorika, Teori Graf</div>
            <div class="session-detail">
              <h4>Cakupan Materi</h4>
              <ul>
                <li>Induksi matematika lemah dan kuat</li>
                <li>Well-Ordering Principle dan relasi rekurensi</li>
                <li>Prinsip inklusi-eksklusi dan pigeonhole</li>
                <li>Teori graf: Euler, Hamilton, pohon</li>
                <li>Semua teknik pembuktian dari seluruh modul</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div><!-- end #syllabus -->

  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:var(--gold)"></div> Klik pertemuan untuk detail topik</div>
    <div class="legend-item"><div class="legend-dot" style="background:var(--red)"></div> Sesi dengan pembuktian utama</div>
    <div class="legend-item"><div class="legend-dot" style="background:var(--blue)"></div> Sesi ujian (UTS / UAS)</div>
  </div>

  <footer>
    <span>Matematika Diskrit &nbsp;·&nbsp; 16 Pertemuan</span>
    <span id="expandCount">0 / 16 topik dijelajahi</span>
  </footer>

</div><!-- end .container -->

<script>
  // Build progress pips
  const progressTrack = document.getElementById('progressTrack');
  for (let i = 1; i <= 16; i++) {
    const pip = document.createElement('div');
    pip.className = 'progress-pip' + (i === 8 || i === 16 ? ' exam' : '');
    pip.dataset.label = i === 8 ? 'UTS' : i === 16 ? 'UAS' : `Prt. ${String(i).padStart(2,'0')}`;
    pip.dataset.session = i;
    pip.addEventListener('click', () => {
      const target = document.querySelector(`[data-session="${i}"]`);
      if (target) { target.scrollIntoView({ behavior: 'smooth', block: 'center' }); target.click(); }
    });
    progressTrack.appendChild(pip);
  }

  let expandedCount = 0;
  const expandCountEl = document.getElementById('expandCount');

  // Session click to expand/collapse
  document.querySelectorAll('.session').forEach(session => {
    session.addEventListener('click', function() {
      const wasExpanded = this.classList.contains('expanded');
      this.classList.toggle('expanded');
      const num = this.dataset.session;
      const pip = document.querySelector(`.progress-pip[data-session="${num}"]`);

      if (!wasExpanded) {
        expandedCount++;
        if (pip && !pip.classList.contains('exam')) pip.classList.add('active');
      } else {
        expandedCount--;
        if (pip && !pip.classList.contains('exam')) pip.classList.remove('active');
      }
      expandCountEl.textContent = `${expandedCount} / 16 topik dijelajahi`;

      // Re-render MathJax for expanded content
      if (typeof MathJax !== 'undefined') MathJax.typesetPromise([this]);
    });
  });

  // Filter buttons
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      const filter = this.dataset.filter;

      document.querySelectorAll('.session').forEach(s => {
        if (filter === 'all' || s.dataset.tag === filter) {
          s.classList.remove('hidden');
        } else {
          s.classList.add('hidden');
        }
      });

      // Show/hide modules based on visible sessions
      document.querySelectorAll('.module').forEach(mod => {
        const visibleSessions = mod.querySelectorAll('.session:not(.hidden)');
        mod.style.display = visibleSessions.length === 0 ? 'none' : '';
      });
    });
  });
</script>
</body>
</html>
    '''
        st.components.v1.html(tulisanHTML,height=6000)
    if menu2[1]:
        tulisanHTML = '''
        <iframe src="https://drive.google.com/file/d/1TyeaVyc5vUGQs_2RDZi7coimKa8mfZbW/preview" style="width:100%; height:2000px"></iframe>
        '''
        st.components.v1.html(tulisanHTML,height=2000)
        tulisanHTML1 = '''
        <iframe src="https://drive.google.com/file/d/1-V8jWTdfJdPpSOnJmzeJlcNANTBzWZ2H/preview" style="width:100%; height:2000px"></iframe>
        '''
        st.components.v1.html(tulisanHTML1,height=2000)
        tulisanHTML2 = '''
        <iframe src="https://drive.google.com/file/d/1-V8jWTdfJdPpSOnJmzeJlcNANTBzWZ2H/preview" style="width:100%; height:2000px"></iframe>
        '''
        st.components.v1.html(tulisanHTML2,height=2000)

#----------Pertemuan 1+++++++++
def materi1():
    st.markdown('''
        <div id="pert1">Logika Proposisi dan Ekuivalensi Logis</div>''',
                unsafe_allow_html=True)
    st.subheader("Test Diagnosa")
    with st.expander("Test Diagnosa"):
        st.title("Diagnosis Logika Matematika")
        nama = st.text_input("Masukkan Nama:")
        soal = {
            "1": ("Negasi dari 'Semua mahasiswa lulus ujian' adalah...",
                  ["Semua mahasiswa tidak lulus ujian",
                   "Ada mahasiswa yang tidak lulus ujian",
                   "Tidak semua mahasiswa tidak lulus",
                   "Ada mahasiswa yang lulus"],
                  "Ada mahasiswa yang tidak lulus ujian"),

            "2": ("Nilai p ∧ q jika p benar dan q salah adalah...",
                  ["Benar", "Salah"],
                  "Salah"),

            "3": ("Nilai p ∨ q jika p benar dan q salah adalah...",
                  ["Benar", "Salah"],
                  "Benar"),

            "4": ("Nilai p → q jika p benar dan q salah adalah...",
                  ["Benar", "Salah"],
                  "Salah"),

            "5": ("Nilai p ↔ q jika p benar dan q benar adalah...",
                  ["Benar", "Salah"],
                  "Benar"),

            "6": ("Konvers dari 'Jika hujan maka jalan basah' adalah...",
                  ["Jika jalan basah maka hujan",
                   "Jika tidak hujan maka jalan tidak basah",
                   "Jika jalan tidak basah maka tidak hujan",
                   "Hujan jika dan hanya jika jalan basah"],
                  "Jika jalan basah maka hujan"),

            "7": ("Nilai ~(p ∧ q) jika p benar dan q salah adalah...",
                  ["Benar", "Salah"],
                  "Benar"),

            "8": ("Nilai x yang memenuhi x + 2 = 5 adalah...",
                  ["2", "3", "5", "7"],
                  "3"),

            "9": ("Negasi dari 'Semua bilangan genap habis dibagi 2' adalah...",
                  ["Semua bilangan genap tidak habis dibagi 2",
                   "Ada bilangan genap yang tidak habis dibagi 2",
                   "Tidak ada bilangan genap yang habis dibagi 2",
                   "Semua bilangan tidak genap habis dibagi 2"],
                  "Ada bilangan genap yang tidak habis dibagi 2"),

            "10": ("Jika belajar maka lulus. Belajar. Kesimpulan...",
                   ["Tidak lulus", "Lulus", "Tidak belajar", "Tidak dapat ditentukan"],
                   "Lulus")
        }

        jawaban_user = {}
        skor = 0

        for key in soal:
            pertanyaan, opsi, kunci = soal[key]
            jawaban = st.radio(pertanyaan, opsi, key=key)
            jawaban_user[key] = jawaban
            if jawaban == kunci:
                skor += 10

        if st.button("Kirim Hasil"):
            st.success(f"Skor Anda: {skor}")

            # GANTI dengan link prefill Google Form Anda
            google_form_url = f"https://docs.google.com/forms/d/e/1FAIpQLSdJlgrGB4KN6JGGdHPsH3lWXoPHoZv5K64RD4u2nDOWuzvxPQ/viewform?usp=pp_url&entry.185074019={nama}&entry.1678102315={skor}"

            st.markdown(f"[Klik di sini untuk menyimpan hasil ke Google Form]({google_form_url})")
    st.header("1. Dasar Teori: Apa itu Proposisi?")
    st.markdown('''
    <div class="konsep1">
    <div>Proposisi adalah pernyataan deklaratif bernilai <b>Benar (True/T)</b> atau
    <b>Salah (False/F)</b>, tetapi tidak keduanya sekaligus</div>
    <div> contoh </div>
    <div>
        <ul type="circle">
        <li>
            "2+2=4" (Proposisi - Benar)
        </li>
        <li>
            "Jakarta adalah ibu kota Jepang(Proposisi - Salah)
        </li>
        <li>
            "x + 2 = 5" (Bukan proposisi, karena nilai kebenarannya bergantung pada x
        </li>
        </ul>
    </div>
    </div>
    ''',unsafe_allow_html=True)
    st.header("2. Penghubung Logika (Operator)")
    st.markdown('''
    <div class="konsep1"> Untuk membangun pernyataan yang lebih kompleks, kita menggunakan operator: </div>
    ''',unsafe_allow_html=True)
    st.markdown(" ##### 1. Konjungsi $p\land{q}$: Benar hanya jika keduanya benar")
    st.markdown('''
    <table>
        <tr>
            <th>p</ht>
            <th>q</hr>
            <th> p &#8743; q </hr>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>True(T)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>False(F)</td>
            <td>False(F)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>True(T)</td>
            <td>False(F)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>False(T)</td>
            <td>False(F)</td>
        </tr>
    </table>
    ''',unsafe_allow_html=True)
    st.markdown(" ##### 2. Disjungsi $p\lor{q}$: Benar hanya jika salah satu atau keduanya benar")
    st.markdown('''
    <table>
        <tr>
            <th>p</ht>
            <th>q</hr>
            <th> p &#8744; q </hr>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>True(T)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>False(F)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>True(T)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>False(T)</td>
            <td>False(F)</td>
        </tr>
    </table>
    ''',unsafe_allow_html=True)
    st.markdown(" ##### 3. Negasi $\lnot{p}$: Kebalikan nilai kebenaran")
    st.markdown('''
    <table>
        <tr>
            <th>p</ht>
            <th>&#172; p</hr>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>False(F)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>True(T)</td>
        </tr>
    </table>
    ''',unsafe_allow_html=True)
    st.markdown(" ##### 4. Implikasi $p\\rightarrow{q}$: Jika p maka q. Salah hanya jika p benar dan q Salah")
    st.markdown('''
    <table>
        <tr>
            <th>p</ht>
            <th>q</hr>
            <th> p &#8594; q </hr>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>True(T)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>False(F)</td>
            <td>False(F)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>True(T)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>False(T)</td>
            <td>True(T)</td>
        </tr>
    </table>
    ''',unsafe_allow_html=True)
    st.markdown(" ##### 5. Konjungsi $p\leftrightarrow{q}$: Benar hanya jika keduanya memiliki nilai yang sama")
    st.markdown('''
    <table>
        <tr>
            <th>p</ht>
            <th>q</hr>
            <th> p &#8596; q </hr>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>True(T)</td>
            <td>True(T)</td>
        </tr>
        <tr>
            <td>True(T)</td>
            <td>False(F)</td>
            <td>False(F)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>True(T)</td>
            <td>False(F)</td>
        </tr>
        <tr>
            <td>False(F)</td>
            <td>False(T)</td>
            <td>True(T)</td>
        </tr>
    </table>
    ''',unsafe_allow_html=True)
    st.header("3. Ekuivalensi Logis")
    st.subheader("Dua pernyataan majemuk dikatakan Ekuivalen secara Logis jika keduanya memiliki nilai kebenaran yang sama di setiap baris tabel kebenaran.")
    st.markdown("#### Hukum-Hukum Penting untuk Pembuktian:")
    st.markdown("""
                ##### 1. Hukum De Morgan:
                >* $\\neg{(p\land{q})}\equiv{\\neg{p}\lor{\\neg{q}}}$
                >* $\\neg{(p\lor{q})}\equiv{\\neg{p}\land{\\neg{q}}}$
                """)
    st.markdown("""
                ##### 2. Hukum Distributif:
                >* $p\lor{(q\land{r})}\equiv{(p\lor{q})\land{(p\lor{r})}}$
                >* $p\land{(q\lor{r})}\equiv{(p\land{q})\lor{(p\land{r})}}$
                """)
    st.markdown("""
                ##### 3. Hukum Implikatif:
                >* $p\\to{q}\equiv{\\neg{p}\lor{q}}$
                >* $p\\to{q}\equiv{\\neg{q}\\to{\\neg{p}}}$
                """)
    st.markdown("""
                ##### 4. Hukum Komutatif (Commutative Laws)
                >* $p\lor{q}\equiv{q\lor{p}}$
                >* $p\land{q}\equiv{q\land{p}}$
                """)
    st.markdown("""
                ##### 5. Hukum Asosiatif (Assosiative Laws)
                >* $p\lor{(q\lor{r})}\equiv{(p\lor{q})\lor{r}}$
                >* $p\land{(q\land{r})}\equiv{(p\land{q})\land{r}}$
                """)
    st.markdown("""
                ##### 6. Hukum Identitas (Identity Laws)
                >* $p\land{T(Benar/True)}\equiv{p}$
                >* $p\lor{F(Salah/False)}\equiv{p}$
                """)
    st.markdown("""
                ##### 7. Hukum Dominasi / Ikatan (Domination Laws)
                >* $p\lor{T(Benar/True)}\equiv{T(Benar/True)}$
                >* $p\land{F(Salah/False)}\equiv{F(Salah/False)}$
                """)
    st.markdown("""
                ##### 8. Hukum Dominasi / Ikatan (Domination Laws)
                >* $p\lor{p}\equiv{p}$
                >* $p\land{p}\equiv{p}$
                """)
    st.markdown("""
                ##### 9. Hukum Negasi Ganda (Double Negation Law)
                >* $\\neg{(\\neg{p})}\equiv{p}$
                """)
    st.markdown("""
                ##### 10. Hukum Komplemen / Negasi (Negation Laws)
                >* $p\lor{\\neg}\equiv{T (Tautologi)}$
                >* $p\land{\\neg}\equiv{F (Kontradiksi)}$
                >* $\\neg{T}\equiv{F}$
                >* $\\neg{F}\equiv{T}$
                """)
    st.markdown("""
                ##### 11. Hukum Absorpsi / Penyerapan (Absorption Laws)
                >* $p\lor{(p\land{q})}\equiv{p}$
                >* $p\land{(p\lor{q}}\equiv{p}$
                """)
    st.markdown("""
                ##### 12. Ekuivalensi Bi-implikasi (Biconditional Equivalences)
                >* $p\leftrightarrow{q}\equiv{(p\\to{q})\land{(q\\to{p})}}$
                >* $p\leftrightarrow{q}\equiv{(\\neg{p}\lor{q})\land{(\\neg{q}\lor{p})}}$
                >* $p\leftrightarrow{q}\equiv{p\land{q})\lor{(\\neg{p}\lor{\\neg{q}})}}$
                """)
    st.header("Latihan")
    st.subheader("20 soal isian yang berfokus pada teknik pembuktian, manipulasi aljabar proposisi, dan deduksi logis.")
    st.subheader("Bagian 1: Ekuivalensi dan Aljabar Logika")
    st.markdown(">* ##### Tentukan bentuk paling sederhana dari pernyataan $\\neg(p\lor(\\neg{p}\land{q}))$ menggunakan hukum-hukum logika.")
    st.markdown(">* ##### Gunakan hukum De Morgan dan distributif untuk menunjukkan bahwa $(p \land q) \lor (p \land \\neg q)$ ekuivalen dengan variabel tunggal apa?")
    st.markdown(">* ##### Dalam pembuktian aljabar, langkah apa yang digunakan untuk mengubah $(p \\rightarrow q)$ menjadi $(\\neg p \lor q)$? Sebutkan nama hukumnya.")
    st.markdown(">* ##### Sederhanakan ekspresi $[(p \\rightarrow q) \land \\neg q]$ menjadi bentuk yang paling ringkas.")
    st.markdown(">* ##### Jika $p \oplus q$ (XOR) didefinisikan sebagai $(p \lor q) \land \\neg(p \land q)$, tuliskan bentuk ekuivalennya hanya dengan menggunakan operator $\\neg$ dan $\\leftrightarrow$.")
    st.markdown(">* ##### Buktikan secara singkat mengapa $p \\rightarrow (q \\rightarrow r)$ ekuivalen dengan $(p \land q) \\rightarrow r$")
    st.markdown(">* ##### Identifikasi hukum logika yang menyatakan bahwa $p \lor (p \land q) \equiv p$.")
    st.markdown(">* ##### Berikan satu contoh bentuk pernyataan yang merupakan kontradiksi namun melibatkan variabel $p$ dan $q$.")
    st.markdown(">* ##### Ubah pernyataan $\\neg p \\rightarrow (q \land \\neg q)$ menjadi bentuk yang lebih sederhana tanpa menggunakan simbol implikasi.")
    st.markdown(">* ##### Jika $A \equiv B$, apakah $\\neg A \\leftrightarrow \\neg B$ selalu merupakan tautologi? Berikan alasannya.")
    st.subheader("Bagian 2: Analisis Argumen dan Metode Pembuktian")
    st.markdown(">* ##### Dalam metode Pembuktian Kontraposisi, jika kita ingin membuktikan Jika $n^2$ genap, maka $n$ genap, apa asumsi awal yang harus kita buat?")
    st.markdown(">* ##### Apa perbedaan mendasar antara asumsi dalam Pembuktian Langsung dengan Pembuktian Kontradiksi (Reductio ad Absurdum)?")
    st.markdown(">* ##### Sebutkan struktur logis dari argumen Silogisme Disjungtif.")
    st.markdown(">* ##### Diberikan premis: $p \\rightarrow q$ dan $\\neg q$. Berdasarkan aturan inferensi Modus Tollens, apa kesimpulan yang sah?")
    st.markdown(">* ##### Mengapa pernyataan $(p \\rightarrow q) \land (q \\rightarrow p)$ disebut sebagai definisi dari bi-implikasi? Analisis dari sisi tabel kebenaran.")
    st.markdown(">* ##### Dalam argumen $[(p \lor q) \land \\neg p] \\rightarrow q$, jelaskan mengapa jika $p$ bernilai benar, argumen tersebut tetap merupakan tautologi.")
    st.markdown(">* ##### Apa yang dimaksud dengan Fallacy of Affirming the Consequent? Tuliskan bentuk notasinya.")
    st.markdown(">* ##### Berikan analisis mengapa implikasi $p \\rightarrow q$ selalu bernilai benar jika $p$ salah, terlepas dari nilai kebenaran $q$.")
    st.markdown(">* ##### Jika kita ingin membuktikan bahwa suatu pernyataan adalah Tautologi menggunakan pohon semantik (truth tree), apa hasil akhir yang harus dicapai pada semua cabang?")
    st.markdown(">* ##### Susunlah sebuah argumen logis yang terdiri dari 3 premis yang menghasilkan kesimpulan $r$, dengan melibatkan operator implikasi dan Modus Ponens.")
    st.header("Koding Bantuan")
    st.code('''
    Function HITUNG_LOGIKA(ByVal rumus As String, p As Boolean, Optional q As Boolean = False, Optional r As Boolean = False) As Variant
    Dim ekspresi As String
    ekspresi = LCase(rumus)
    ' 1. Ganti variabel dengan angka (1 untuk True, 0 untuk False)
    ' Ini lebih stabil untuk fungsi Evaluate di Excel
    ekspresi = Replace(ekspresi, "p", IIf(p, "1", "0"))
    ekspresi = Replace(ekspresi, "q", IIf(q, "1", "0"))
    'ekspresi = Replace(ekspresi, "r", IIf(r, "1", "0"))
    
    ' 2. Ganti operator logika manusia ke format yang dipahami Excel
    ' Kita gunakan fungsi Excel karena Evaluate memproses string sebagai rumus Excel
    ekspresi = Replace(ekspresi, "<->", "=")
    ekspresi = Replace(ekspresi, "->", "<=")
    ekspresi = Replace(ekspresi, "not", " NOT ")
    ekspresi = Replace(ekspresi, "and", " * ")
    ekspresi = Replace(ekspresi, "or", " + ")
    ekspresi = Replace(ekspresi, "xor", " <> ")
    
    ' 3. Eksekusi sebagai rumus Excel
    On Error GoTo TanganiError
    HITUNG_LOGIKA = Evaluate(ekspresi)
    
    ' Konversi kembali angka 0/-1 menjadi Boolean True/False
    If IsNumeric(HITUNG_LOGIKA) Then
        HITUNG_LOGIKA = CBool(HITUNG_LOGIKA)
    End If
    Exit Function

TanganiError:
    HITUNG_LOGIKA = "Error: Cek Penulisan"
End Function
    ''')
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1772463792/gambar1_fjttju.png")
#=====Pertemuan kedua++++

def materi2():
    menu1 = st.tabs(['pretest','Materi','Media Aplikasi','postest'])
    with menu1[0]:
        tulisanHTML = '''
        <iframe src="https://martin-bernard26.github.io/matematikaDiskrit2023A1/petestKuantor.html" style="width:100%; height:2000px"></iframe>
        '''
        st.components.v1.html(tulisanHTML,height=2000)
    with menu1[1]:
        tulisanHTML = '''
        <iframe src="https://martin-bernard26.github.io/matematikaDiskrit2023A1/setiap.html" style="width:100%; height:2000px"></iframe>
        '''
        st.components.v1.html(tulisanHTML,height=2000)
    with menu1[2]:
        st.title("Kalkulator cek kebenaran")
        st.subheader("Gunakan variabel p, q, r, s")
        st.subheader("Gunakan fungsi Konjungsi: And(p,q)")
        st.subheader("Gunakan fungsi Disjungsi: Or(p,q)")
        st.subheader("Gunakan fungsi Implikasi: Implies(p,q)")
        st.subheader("Gunakan fungsi Biimplikasi: Equivalent(p,q)")
        p, q, r, s = sp.symbols(r'p q r s')
        masukan = st.text_input("Penyederhanaan Operasi Logika")
        if masukan:
            hasil = sp.simplify(masukan)
            hasil1 = sp.latex(simplify_logic(hasil))
            st.latex(hasil1)
    with menu1[3]:
        tulisanHTML = '''
        <iframe src="https://martin-bernard26.github.io/matematikaDiskrit2023A1/posttestKuantor.html" style="width:100%; height:2000px"></iframe>
        '''
        st.components.v1.html(tulisanHTML,height=2000)
    
#======upload++++
def upload_tugas():
    st.title("Upload Jawaban Tulisan Tangan")
    nama = st.text_input("Nama")
    nim = st.text_input("NIM")

    foto = st.camera_input("Foto Jawaban")

    if st.button("Upload"):

        if foto is not None:

            url = "https://api.cloudinary.com/v1_1/ikip-siliwangi/image/upload"

            files = {"file": foto.getvalue()}

            data = {
                "upload_preset": "upload_jawaban",
                "public_id": f"{nama}_{nim}"
            }

            response = requests.post(url, files=files, data=data)

            result = response.json()

            if "secure_url" in result:
                st.success("Upload berhasil")
                st.write(result["secure_url"])
            else:
                st.error("Upload gagal")
                st.write(result)

def kolom_diskusi():
    # URL Firebase Realtime Database
    FIREBASE_URL = "https://vba-modul-diskusi-default-rtdb.firebaseio.com/chat.json"

    st.title("💬 Chatbot Firebase + Streamlit")

    # session chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # fungsi kirim pesan ke firebase
    def send_message(user, text):
        data = {
            "user": user,
            "message": text,
            "time": time.time()
        }

        requests.post(FIREBASE_URL, json=data)


    # fungsi ambil pesan
    def get_messages():

        response = requests.get(FIREBASE_URL)

        if response.status_code == 200 and response.json() != None:
            data = response.json()
            return list(data.values())

        return []


    # input nama
    username = st.text_input("Nama Anda")

    # tampilkan pesan
    messages = get_messages()

    for msg in messages:
        st.write(f"**{msg['user']}** : {msg['message']}")

    # input chat
    chat = st.text_input("Tulis pesan")
    if st.button("Kirim"):
        if username and chat:
            send_message(username, chat)
            st.rerun()
#--------------------------------------
if st.session_state.kondisi['kover']:
    pendahuluan()
if st.session_state.kondisi['pertemuan1']:
    materi1()
if st.session_state.kondisi['pertemuan2']:
    materi2()
if st.session_state.kondisi['pertemuan3']:
    upload_tugas()
if st.session_state.kondisi['pertemuan4']:
    kolom_diskusi()
#--------------------------------------
if st.sidebar.button('Pendahuluan'):
    st.session_state['kondisi'] = {"kover":True,"pertemuan1":False, "pertemuan2":False,
                                   "pertemuan3":False,"pertemuan4":False}
    st.rerun()
if st.sidebar.button('Upload Tugas'):
    st.session_state['kondisi'] = {"kover":False,"pertemuan1":False, "pertemuan2":False,
                                   "pertemuan3":True,"pertemuan4":False}
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button('Pertemuan 1'):
    st.session_state['kondisi'] = {"kover":False,"pertemuan1":True, "pertemuan2":False,
                                   "pertemuan3":False,"pertemuan4":False}
    st.rerun()
if st.sidebar.button("Pertemuan 2"):
    st.session_state['kondisi'] = {"kover":False,"pertemuan1":False, "pertemuan2":True,
                                   "pertemuan3":False,"pertemuan4":False}
    st.rerun()
st.sidebar.markdown("---")
if st.sidebar.button("Tempat Diskusi"):
    st.session_state['kondisi'] = {"kover":False,"pertemuan1":False, "pertemuan2":False,
                                   "pertemuan3":False,"pertemuan4":True}
    st.rerun()
    
