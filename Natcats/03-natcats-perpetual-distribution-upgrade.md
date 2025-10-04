# Natcats P2P Perpetual Distribution Upgrade  

Natcats will enable **P2P Perpetual Distribution** (P2PPD) beginning at Bitcoin block **919296**. As of this block, all future Natcats supply produced by the Bitcoin blockchain will be issued directly to Natcats holders.  

All P2PPD distribution and indexing systems are deployed fully on-chain on **Ordinals**, ensuring the **decentralized production** of Bitcoin’s first natively generated art collection over the years to come.  

---

## Supply & Allocation  
- Natcats are produced when the pattern 3b occurs in the hexadecimal representation of Bitcoin’s block difficulty data. This property is rare and has occurred only four times in Bitcoin’s history. Each occurrence produces **2,016 Natcats**.
- **Prior to the update**, new supply would become available via open mint, a process that is vulnerable to bot minting and allocation outside of the holder base. **As of the update**, each new Natcat will instead be allocated automatically to a specific Natcat holder.
- When a Bitcoin block produces a Natcat, the block’s hash is used as a deterministic seed to randomly select from a pool of all prior Natcats. The selected Natcat becomes the **authorized parent** for the new Natcat.
- The holder of the authorized parent has exclusive rights to inscribe the new asset. All other attempts will be rejected by on-chain indexing and will not render.  
- New Natcats are added to the index and the pool automatically, and become eligible to win Natcats on future blocks.
- Mint rights do not expire, and transfer with a parent Natcat until utilized. 
- The system is operated autonomously on-chain, without centralized dependencies.

---

## Indexing  
- The **Natcats index** updates automatically on-chain as new assets are inscribed, published at:  
  [`765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)  
- For instructions on how to query the Natcats on-chain index and/or generate a local copy, see the [Perpetual Distribution documentation](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md) (*see “How to Query Index” section*).  
- The on chain index serves as the authorative index moving forward. The prior **TAP Protocol index** is valid up to block **919295**, and above this block is not authorative.  



---

## Minting  
- New supply can be inscribed via inscription tools that provide full support for **Ordinals protocol v2.2.1 or later**.  
- There is **no mint fee**, though platform service fees may apply.  
- Follow detailed instructions [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md#minting-instructions) to mint with the correct parameters and syntax.  


---

## Rendering  
- **Generations 5+** render natively in Ordinals explorers by default once inscribed.  
- **Generations 1–4** render via the preexisting UNAT pathway (requires UNAT specific wallet support), but can optionally be **reinscribed** to enable native rendering.  
- Reinscriptions are **permanently packaged with the canonical inscription’s sat** and will travel together in perpetuity.  
<!-- - See [How to Enable Gen 1–4 Native Rendering](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md) for reinscription instructions.  --->
- Reinscription Instructions can be found at [COMING SOON]

Examples  
- [Gen 1 UNAT Default Inscription](https://ordinals.com/inscription/5c26e644c0a93f02f964182fdab436378405d0f6639ca20134f747b160457e76i0)  
- [Gen 1 UNAT Native Render Inscription](https://ordinals.com/inscription/4d71c795bf62a1a458c5411b2b2ab0cb35209bb0ed7b5614a401ec781beadbbfi0)  

---

## Treasury  
- Ten percent (10%) of new Natcats are allocated to a Natcats Treasury, to enable a combination of long term holding, partnerships, sales, and acquisitions in support of the project’s legacy.  

---

## Holder Action  
- **No action is required** from holders.  
