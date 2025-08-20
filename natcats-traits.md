# Natcats Traits  

The data properties of a Natcat's Bitcoin block number determine its unique traits.  

---

## Special Traits  

Special traits are found when a Natcat's Bitcoin block is a match for specific patterns.  

For example:  
- The trait **Catnip Cig** appears when the block number contains **"420"**.  
- Block **42420** contains "420", so it generates a **Catnip Cig**.  

| Trait                | Bitcoin Block Condition            | Supply | Example  |
|----------------------|-----------------------------------|--------|----------|
| Cig                  | contains "4" & "0"                | 1,446  | 42340    |
| Catnip Cig           | contains "420"                    | 38     | 42420    |
| Rainbow Collar       | is multiple of 12                 | 672    | 42336    |
| Pearls               | is multiple of 13                 | 620    | 42341    |
| Orange Collar        | is multiple of 14                 | 576    | 42336    |
| Headband             | is multiple of 15                 | 536    | 42345    |
| Sunhat               | is multiple of 16                 | 504    | 42336    |
| Spikes Collar        | is multiple of 69                 | 116    | 42366    |
| Mouse                | is multiple of 11 but not 888     | 731    | 42339    |
| Alien Mouse          | is multiple of 888                | 8      | 42624    |
| Bow Right            | contains two "8"s                 | 977    | 42388    |
| Bow Left             | contains "88"                     | 244    | 42388    |
| Bow Tail             | contains "888"                    | 17     | 42888    |
| Alien Bow Tie        | contains "8888"                   | 1      | 828888   |
| Double Alien Bow Tie | contains "88888"                  | 0      | Unreleased |
| Trout                | contains two "9"s but not "99"    | 229    | 42909    |
| Salmon               | contains "99" but not "999"       | 227    | 42399    |
| Alien Fish           | contains "999" but not "9999"     | 16     | 42999    |
| Giant Alien Fish     | contains "9999"                   | 1      | 829999   |
| Earring Left         | contains "0" but not "000"        | 2,555  | 42340    |
| Earring Right        | contains "00" but not "0000"      | 241    | 42400    |
| Alien Earring Left   | contains "000"                    | 17     | 43000    |
| Alien Earring Right  | contains "0000"                   | 1      | 830000   |
| Alien Tiara          | contains "00000"                  | 0      | Unreleased |
| Laser Eyes           | contains 4-digit square, look R   | 231    | 42401    |
| Laser Eyes Left      | contains 4-digit square, look L   | 17     | 42640    |
| Laser Eyes Crossed   | contains 4-digit square, look C   | 2      | Unreleased |
| Yarn                 | contains 5-digit square           | 43     | 42436    |
| Laser Pointer        | contains 6-digit square           | 5      | 123201   |
| Fly                  | contains "11"                     | 152    | 42411    |
| Fly w/ Earring       | contains "111" but not "1111"     | 8      | 43111    |
| Fly w/ Alien Earring | contains "1111"                   | 0      | Unreleased |
| Fly w/ Laser Eyes    | contains "11111"                  | 0      | Unreleased |
| Night Vision         | contains power of 7               | 2,509  | 42337    |
| Alien Diamond        | contains 6-digit palindrome       | 7      | 123321   |
| Blood Drips          | contains 3-digit Fibonacci        | 283    | 42336    |
| Brow Piercing        | contains 4-digit Fibonacci        | 4      | 42584    |
| Halo                 | contains 5-digit Fibonacci        | 1      | 828657   |
| Hammer               | contains 6-digit Fibonacci        | 0      | Unreleased |
| Vial                 | contains 7-digit Fibonacci        | 0      | Unreleased |

---

## Color Combination  

The value present in each digit of a block number determines the color for each component of the Natcat.  
Digits are read from **right to left**.  

For example:  
- If the block number is **42340** → the **first digit (from the right)** is `0`.  
- Digit `0` corresponds to **Dark Grey**.  
- So in this case, the **Face** would be Dark Grey.  

### Digit Position → Cat Component
- **Position 1** → Face  
- **Position 2** → Body  
- **Position 3** → Left Ear  
- **Position 4** → Right Ear  
- **Position 5** → Nose  
- **Position 6** → Stripes  
- **Position 7** → Tooth Type  

### Digit → Color

| Digit | Color      | Preview |
|-------|-----------|---------|
| 0     | Dark Grey | ![#545459](https://via.placeholder.com/15/545459/000000?text=+) `#545459` |
| 1     | Purple    | ![#6A45FF](https://via.placeholder.com/15/6A45FF/000000?text=+) `#6A45FF` |
| 2     | Lilac     | ![#B8A5E0](https://via.placeholder.com/15/B8A5E0/000000?text=+) `#B8A5E0` |
| 3     | Yellow    | ![#FFE733](https://via.placeholder.com/15/FFE733/000000?text=+) `#FFE733` |
| 4     | Blue      | ![#1075FF](https://via.placeholder.com/15/1075FF/000000?text=+) `#1075FF` |
| 5     | Brown     | ![#7B543E](https://via.placeholder.com/15/7B543E/000000?text=+) `#7B543E` |
| 6     | Grey      | ![#C5C5D3](https://via.placeholder.com/15/C5C5D3/000000?text=+) `#C5C5D3` |
| 7     | Green     | ![#12C35A](https://via.placeholder.com/15/12C35A/000000?text=+) `#12C35A` |
| 8     | Pink      | ![#FF5DB5](https://via.placeholder.com/15/FF5DB5/000000?text=+) `#FF5DB5` |
| 9     | Orange    | ![#FF5608](https://via.placeholder.com/15/FF5608/000000?text=+) `#FF5608` |
