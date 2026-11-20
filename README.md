# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/pytraaa9-ai/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/pytraaa9-ai/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that writes one image summing up Friday 20 November 2026 world news — a newspaper front page (1024×1024 PNG): lead story Russian missiles hitting three Kyiv bridges, plus 37 more stories across six continents, a world map, and the day's biggest market slide.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The day's news

- **Lead:** Russian missiles hit three Kyiv bridges — Missiles strike three bridges over the Dnipro — Podilsko-Voskresenskyi, Darnytskyi and Pivdennyi — killing 3 and injuring 9–15. Traffic between the river banks is cut; the attack follows Thursday's strikes that killed one and damaged two embassies.
- **Second story:** Poland: airspace violated — Three objects — likely two missiles and a drone — cross into Poland overnight. The defence minister calls it a ‘provocation’; probes open at three sites.
- UK–EU summit in Brussels: Youth mobility scheme expected; food-trade and carbon deals on the table.
- Allies ready for Russia talks: Coalition of the willing meets in Berlin; US envoy floats NATO-style guarantee.
- Italy's general strike: Workers and students march in dozens of cities over wages and living costs.
- 11 nations drill in Poland: European troops rehearse a possible postwar mission in Ukraine.
- French police trial verdict due: Landmark brutality case over the Michel Zecler assault reaches its end.
- Spain's election campaign opens: Vote set for 29 November; PM Sánchez admits his government made ‘mistakes’.
- Denmark oks Greenland deal: Copenhagen approves the agreement with Trump on the Arctic island.
- UK admits Apple backdoor order: London forced to confirm it ordered access to Apple users' data.
- Italy 3–1 France: Azzurri fight back in the Nations League; Zverev and Alcaraz lead in Turin.
- Israel crosses Yellow Line: First ground incursion since the truce; tunnel dismantled, Hamas cries foul.
- Iran war enters month 9: Hormuz tanker attacks intensify; a tanker burns after hitting a mine.
- Senate rejects war limit: US Senate votes 51–48 against curbing the president's Iran war powers.
- Somalia expels UAE envoy: Mogadishu orders the ambassador out, citing an ‘invasion’.
- Ethiopia, Eritrea mass troops: Both sides build up on the border as fears of a new war grow.
- Sudan mine strike kills 10: Drone hits a gold mine in South Kordofan; Amnesty urges a probe.
- Kenya's last Ebola patient out: Country discharges its final case 37 days after the first was found.
- Nigeria ends suicide jail terms: Senate moves to scrap prison for attempted suicide.
- Haiti raid kills 34: Police kill 34 gang members in a capital raid; crowds cheer.
- Senegal boat capsizes: Dozens missing after a migrant boat goes down off Yenne.
- Cyclone Akvan hits India: Third storm in under a month makes landfall on the east coast.
- Xi meets Australian PM: China's leader projects global clout after hosting Trump and Putin.
- Samsung names new chip chief: Memory division gets a new boss in a management reshuffle.
- Sydney car-bomb plot charge: Man charged over a car-bomb plan and Islamic State material.
- Stocks slide again: S&P 500 falls 2% for a fifth day; Nikkei drops 4.8%, SoftBank 16%.
- White House fires cyber chief: Cairncross sacked after a week of tech outages; Microsoft 365 goes down.
- California subpoenas Nvidia: State demands answers on chips to China; Huang resigns, Kress steps in.
- Trump pardons Pete Rose: Baseball's banned hits king is pardoned posthumously.
- U.S. sanctions mafia clans: Comancheros and ‘Ndrangheta hit with asset freezes.
- U.S.–Venezuela sign deal: Washington and Caracas agree a military cooperation pact.
- Bukele seeks third term: El Salvador's president registers to run again.
- Brooklyn collapse kills 8: Building falls in New York; 19 injured in the rubble.
- Florida floods worst on record: St Johns River peaks in catastrophic flooding on the east coast.
- GTA VI tops $2.3bn: Take-Two says launch sales pass $2.3 billion in the first days.
- F1 races in Las Vegas: Pochettino named Manchester United boss; Russell Brand jailed 10 years.
- COP31 draft drops phase-out: Antalya text omits fossil-fuel exit; Pacific nations demand it back.
- Satellites outnumber stars: Orbital craft now top visible stars over most towns, study finds.

All stories were verified against at least two reputable sources
(Reuters, AP, AFP, BBC, Al Jazeera, UN News) on 20 November 2026.
Note: this v1 entry covers the news of Friday 20 November 2026 reported
so far; a full-day v2 entry may replace it before the deadline.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(falling back to `/output/entry.png`). The copy is byte-for-byte, so two
runs always produce identical output.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x9vj0gh6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
