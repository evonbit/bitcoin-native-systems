# Natcats P2P Perpetual Distribution Upgrade  

Natcats will enable **P2P Perpetual Distribution** beginning at Bitcoin block **NNNNNN**. After this upgrade, all future Natcats supply produced by the Bitcoin blockchain will be allocated directly to Natcats holders.  

As of this update, all distribution and indexing systems are deployed fully on-chain on **Ordinals**, without third-party dependencies, ensuring the **decentralized production** of Bitcoin’s first natively generated art collection over the years to come.  

---

## Supply & Allocation  
- New Natcats supply is produced when the substring **“3b”** appears in Bitcoin’s difficulty field. Each supply event produces a **generation of 2,016 Natcats**.  
- Bitcoin difficulty adjusts every **2,016 blocks** (roughly every two weeks) and the Bits field is recalculated at each adjustment, creating a new chance for the “3b” pattern.  
- **As of the upgrade**, when a new generation of Natcats is produced, mint rights for each individual Natcat are assigned automatically to an existing holder via a **block-hash lottery**.  
- The holder of the winning Natcat (the **authorized parent**) has exclusive rights to inscribe the new asset. All other attempts will be rejected by on-chain indexing and will not render.  
- This system is operated autonomously on-chain, without centralized dependencies, and does not expire.  

---

## Minting  
- New supply can be inscribed via inscription tools that provide full support for **Ordinals protocol v2.2.1 or later**.  
- There is **no mint fee**, though platform service fees may apply.  
- Follow detailed instructions [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/Perpetual%20Distribution/01-about-perpetual-distribution.md#minting-instructions) to mint with the correct parameters and syntax.  

---

## Indexing  
- The **Natcats index** updates automatically on-chain as new assets are inscribed, published at:  
  [`765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)  
- For instructions on how to query the Natcats on-chain index and/or generate a local copy, see the [Perpetual Distribution documentation](https://github.com/evonbit/bitcoin-native-systems/blob/main/Perpetual%20Distribution/01-about-perpetual-distribution.md) (*see “How to Query Index” section*).  
- The prior **TAP Protocol index** is valid only up to block **NNNNNN**, and above this block is no longer authorative.  

---

## Rendering  
- **Generations 5+** render natively in Ordinals explorers by default once inscribed.  
- **Generations 1–4** render via the preexisting UNAT pathway (requires UNAT specific wallet support), but can optionally be **reinscribed** to enable native rendering.  
- Reinscriptions are **permanently packaged with the canonical inscription’s sat** and will travel together in perpetuity.  
- See [How to Enable Gen 1–4 Native Rendering](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md) for reinscription instructions.  

---

## Treasury  
- **10% of all future supply issuance** is reserved for the **Natcats Treasury**.  

---

## Holder Action  
- **No action is required** from holders.  
