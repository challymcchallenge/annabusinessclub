---
title: ANNA Business Club · Demo Site V2 (design în stilul playbook-ului)
date: 2026-11-14
status: prototip complet, în așteptarea aprobării (GATE D3)
sursa_continut: 2026_11_14_ANNA_Business_Club_Demo_Site.md (V1, textele celor 31 de ecrane, neschimbate)
template_design: https://claude.ai/artifact/PKvoVrudNvu1xyuquYjGkF (PASUL 1 - ANNA BUSINESS CLUB_V1)
---

# ANNA Business Club · Demo Site V2

V2 păstrează integral conținutul și comportamentul din V1 și schimbă doar stratul vizual, preluat din playbook-ul „PASUL 1 - ANNA BUSINESS CLUB_V1".

## Ce s-a schimbat față de V1

| Element | V1 | V2 |
|---|---|---|
| Fonturi | Cormorant Garamond + Montserrat | Bricolage Grotesque (titluri), Inter (text), JetBrains Mono (etichete, butoane) |
| Paletă | Negru cald + roșu ANNA | Bleumarin (#070d19, #0f172a) + auriu (#f59e0b), cu 6 culori de zonă |
| Navigare | Meniu orizontal sus | Șină lipită în stânga, 260 px, cu puncte colorate; pe telefon devine bară sus |
| Antet | Bară demo + antet alb/negru | Banner bleumarin în degrade, cu linie aurie de 4 px |
| Titlu de pagină | Text simplu | Bandă colorată cu etichetă, ca antetele de secțiune din playbook |
| Casete | Contur simplu, rază 10 px | Margine colorată sus (4 px), culorile se rotesc: auriu, albastru, verde, mov, turcoaz, roz |
| Prima pagină | Coloană cu logo și text | Panou bleumarin cu linie aurie, apoi 4 casete de cifre, apoi secțiuni cu antet colorat |
| Cartela de membru | Negru cu cip auriu | Bleumarin în degrade, contur auriu dublu |
| Subsol | Deschis | Bleumarin, cu linie aurie sus |

## Valorile de design (din template)

| Token | Valoare |
|---|---|
| Fundal / suprafață, temă întunecată | #070d19 / #0f172a |
| Fundal / suprafață, temă deschisă | #f1f5f9 / #ffffff |
| Accent structural | auriu #f59e0b (linii), #d97706 (margini), #92400e (etichete) |
| Roșu ANNA | #c2211f (butonul principal), #e8322e (arcul din logo) |
| Titluri | h1 26–40 px, h2 19–24 px, h3 17 px, greutate 800, spațiere −0,02 em |
| Text | 16 px / 1,6; text mic 13,5 px; etichete mono 11,5 px majuscule |
| Raze | 12 px secțiuni, 10 px casete, 8 px butoane, 6 px etichete |
| Ținte de atingere | minimum 44 px |

Culoarea fiecărei zone: public auriu · acces și profil albastru · evenimente, servicii, anunțuri turcoaz · concurs roz · zona de membru verde · administrare mov.

## Ce a rămas neschimbat

- Toate textele, cifrele și etichetele („exemplu", „de definit", `[ASSUMPTION]`): 282 de fragmente de text comparate automat cu V1, 0 diferențe.
- Cele 31 de ecrane, adresele lor, cele 4 roluri și comutatorul Senior/Junior.
- Fluxurile: invitație → cerere → chestionar → rezultat → candidatură → cartelă; rezervări; cartonașe; înscriere în concurs.
- Logoul E2 (rămâne în Cormorant Garamond, cu arcul roșu), logourile transparente, tema întunecată la pornire, iconițele desenate în pagină.

## Abateri de la meta-prompt, de confirmat

1. Roșul ANNA nu mai este accentul principal al interfeței. Template-ul cere auriu pe bleumarin; roșul a rămas pe logo și pe butonul principal.
2. Tema de pornire este bleumarin foarte închis (#070d19), nu negru.
3. Pașii D1 (3 direcții) și D2 (3 ecrane) au fost săriți, pentru că direcția a fost dată prin template.

## Verificare

496 de combinații deschise automat (31 de ecrane × 4 roluri × 400 px și 1366 px × 2 teme): fără erori de script, fără derulare orizontală, fără ținte sub 44 px. Contrastul nu a fost măsurat automat; culorile de text vin din template, care le declară la minimum 4,5:1.

## Cum se reface

V2 se generează din V1 cu două fișiere: `v2.css` (foaia de stil nouă) și `build.py` (înlocuiește stilul, structura paginii și 6 linii din script). Dacă se schimbă un text în V1, se rulează din nou `build.py`.

---
100% AI Solutions & Agentic Work-Flows for SMEs
Made with ❤️ by BizTech Consulting SRL
Alin Labau - AI Project Manager | +40 772 295 031 | www.biztech.ro
