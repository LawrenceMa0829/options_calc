write me a streamlit app as below requirements in sequence:

1. Title is "Options Calc"
2. Subtitle is "Sell Iron Condor - Stable Profit"
3. "每張合約（股）", 100 as variable, visualize and uneditable
4. "Spread 寬度", 2 as variable, , visualize and editable. step +1/-1
5. "多少張合約", 1 as variable, , visualize and editable. step +1/-1
6. "向下Spread (-)", 20 as variable, , visualize and editable. step +1/-1
7. "向上Spread (+)", 15 as variable, , visualize and editable. step +1/-1
8. "QQQ 現價", 600 as variable, , visualize and editable. step +1/-1
9. <BR>
10. Create a table (10 to 18 is table) with header as below: item, DTE, QQQ price, 期權金, 平倉位
11. "long put (Buy)↓P", "(60DTE)", QQQ 現價-向下Spread (-)-Spread 寬度-14, 18.52, CONCAT("< ",ROUNDUP(QQQ price-期權金-3))
12. <BR>
13. "long put (Buy)↓P", "(2DTE)", QQQ 現價-向下Spread (-)-Spread 寬度, 1.3, blank
14. "short put (Sell)↓P", "(2DTE)", QQQ 現價-向下Spread (-), 1.49, set it QQQ 現價-向下Spread (-)+1
15. "short call (Sell)↓C", "(2DTE)", QQQ 現價+向上Spread (+), 0.93, QQQ 現價+ QQQ 現價+向上Spread (+)-1
16. "long call (Buy)↑C", "(2DTE)", QQQ 現價+向上Spread (+)+Spread 寬度, 0.63, blank
17. <BR>
18. "long call (Buy)↑C", "(60DTE)", QQQ 現價+向上Spread (+)+Spread 寬度+14, 18.35, CONCAT("> ",ROUNDUP(QQQ price+期權金+3,0))
19. <BR>
20. "Net Credit", (QQQ 現價-向下Spread (-) + QQQ 現價+向上Spread (+) - QQQ 現價-向下Spread (-)-Spread 寬度 - QQQ 現價+向上Spread (+)+Spread 寬度) * 每張合約（股）
21. "Net Credit x 100 - Transaction Fee", 每張合約（股）* Net Credit - 10.5, USD
22. "Potential Loss", 每張合約（股）*Spread 寬度*多少張合約-Net Credit x 100 - Transaction Fee, USD
23. <BR>
24. "長期 OTM 保險腿成本", ("long put (Buy)↓P", "(60DTE)"期權金 + "long call (Buy)↑C", "(60DTE)"期權金) * 每張合約（股）, USD

P.S.1: For above points 10 to 18, 期權金 are the only textbox for editable. step +0.1/-0.1. item and DTE are hardcoded. QQQ price and 平倉位 are formulas or left blanks
P.S.2: All the number once inputted, need to update the formula instantly and automatically without manually refresh and wait like Excel.