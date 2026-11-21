# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/pytraaa9-ai/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/pytraaa9-ai/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that writes one image summing up Friday 20 November 2026 world news — a newspaper front page (1024×1024 PNG): lead story Russian missiles hitting three Kyiv bridges (updated toll: 7 killed in Kyiv, 9 across Ukraine), plus 37 more stories across six continents, a world map, and Friday's AI-driven market rout. Full-day v2 edition — supersedes the partial-day v1.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The day's news

- **Lead:** Russian missiles hit three Kyiv bridges — Missiles strike three bridges over the Dnipro — Podilsko-Voskresenskyi, Darnytskyi and Pivdennyi — killing 7 in Kyiv, 9 across Ukraine, and injuring 17. Barrage: 84 cruise missiles, 404 drones, 27 ballistic missiles; traffic back on one bridge by 15:00.
- **Second story:** Poland: missiles crash in — Two Russian Kh-101 missiles and a jet-powered drone crash in south-east Poland during the assault. NATO scrambles jets; probes open at three sites.
- UK–EU summit deal in principle: Youth mobility quota ~100,000 a year; apply by 2028, full access by Jan 2030.
- Allies ready for Russia talks: Berlin summit: Europe ready to talk; Kushner says Trump open to NATO-style guarantee.
- Italy's general strike: 1m+ march in 100+ cities over wages; youth walkouts in 25+ countries.
- Ukraine deploys laser defence: Laser defence debuts in Kyiv; Druzhba pipeline struck in Tatarstan.
- UNICEF: 1,144 children hit: Children killed or injured in Ukraine Jan–Oct 2026, highest in 3 years.
- Estonia to close Russian border: Road crossings shut over ‘sustained aggression’.
- Denmark: spy plot, Greenland deal: Expels Russian defence attaché over Kyivstoner plot; approves Trump deal.
- France approves police law: Senate backs presuming officers acted lawfully; Zecler verdict awaited.
- Spain's election campaign opens: Vote set for 29 November; PM Sánchez admits ‘mistakes’.
- UK admits Apple backdoor order: London forced to confirm it ordered access to Apple users' data.
- Italy 3–1 France: Azzurri fight back in the Nations League; Zverev and Alcaraz lead in Turin.
- Israel crosses Yellow Line: First incursion since the truce; tunnel dismantled; baby dies of hypothermia.
- Iran war enters month 9: Hormuz tanker attacks intensify; a tanker burns after hitting a mine.
- Trump weighs new Iran strikes: US and Israeli officials press him to act before year-end.
- Saudi intercepts Houthi attack: Missile and drones downed over the south, a day after the Riyadh tower hit.
- Somalia expels UAE envoy: Mogadishu orders the ambassador out, citing an ‘invasion’.
- Ethiopia, Eritrea mass troops: Both sides build up on the border as fears of a new war grow.
- Sudan mine strike kills 10: Drone hits a gold mine in South Kordofan; Amnesty urges a probe.
- Kenya's last Ebola patient out: Country discharges its final case 37 days after the first was found.
- Nigeria ends suicide jail terms: Senate moves to scrap prison for attempted suicide.
- Senegal boat capsizes: Dozens missing after a migrant boat goes down off Yenne.
- Cyclone Akvan hits India: Landfall near Gopalpur, Odisha; 300,000+ evacuated; no deaths at first.
- Xi meets Australian PM: China's leader projects global clout after hosting Trump and Putin.
- Samsung names new chip chief: Memory division gets a new boss in a management reshuffle.
- Sydney car-bomb plot charge: Man charged over a car-bomb plan and Islamic State material.
- New Zealand thrash India: Visitors win by 244 runs in the cricket series.
- AI rout: S&P −3.70%, Nasdaq −5.28%: Seventh straight loss, into correction; Nvidia −14% on SEC probe.
- Trump threatens data-centre tax: ‘Tremendous tax’ on US tech firms building AI centres abroad.
- Nvidia probe deepens: SEC probes accounting; Huang resigns, Kress steps in.
- Cyber chief fired, Microsoft down: Cairncross sacked after a week of outages; 365 outage hits Outlook, Teams.
- Bayer's $7.25bn Roundup deal: Missouri judge approves the settlement over weedkiller claims.
- Pete Rose pardoned: Trump posthumously pardons baseball's banned hits king.
- Brooklyn collapse kills 8: Building falls in New York; 19 injured. Florida floods worst on record.
- GTA VI tops $2.3bn: Take-Two launch sales pass $2.3bn; Rosalía makes Latin Grammy history.
- COP31: no deal in Antalya: Final day runs into overtime; draft drops fossil-fuel phase-out and $120bn target.
- Satellites outnumber stars: Orbital craft now top visible stars over most towns; Meta rethinks 2030 goals.

All stories were verified against at least two reputable sources
(Reuters, AP, AFP, BBC, Al Jazeera, UN News) on 20 November 2026.
This v2 entry covers the full day of Friday 20 November 2026 and
supersedes the partial-day v1 entry.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(falling back to `/output/entry.png`). The copy is byte-for-byte, so two
runs always produce identical output.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x9vj0gh6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
