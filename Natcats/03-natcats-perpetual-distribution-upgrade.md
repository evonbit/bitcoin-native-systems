# P2P Perpetual Distribution Update

As of Bitcoin block **919296**, all future Natcats supply will be automatically issued to Natcats holders through a **decentralized on-chain distribution system**.  

Natcats will enable **P2P Perpetual Distribution**, a Bitcoin-native distribution model developed by **@evonbit**.  
P2P Perpetual Distribution (P2PPD) automatically allocates mint rights for new Natcats supply among holders as it is produced by the Bitcoin Blockchain.  

The system operates **autonomously on Bitcoin Ordinals** and in perpetuity—**without dependencies on third-party indexers or authorities**.  

---

## Allocation
- Natcats are produced when the pattern **3b** occurs in the hexadecimal representation of Bitcoin’s block difficulty data — a rare event that has occurred only **four** times in Bitcoin’s history. Each occurrence produces **2,016 Natcats**.  
- When a Bitcoin block produces a new Natcat, the **block hash** is used to **select from a pool of all prior Natcats via an on-chain lottery**.  
- The selected Natcat becomes the **authorized parent** for the new cat.  
- Only the **holder of the authorized parent** can inscribe the new Natcat; all other inscription attempts are **rejected from indexing and will not render**, enforced by the on-chain system.  
- As new supply is inscribed, it is **automatically added to the on-chain index**, which operates in perpetuity.  
- Newly inscribed Natcats are **immediately added to the pool** and become eligible to win future Natcats blocks.  
- Each Natcat held has an **equal chance** of winning new supply, and a holder’s chances increase **proportionally** as more Natcats are owned.  
- This model eliminates all risk of **bot minting** and ensures new supply remains **within the holder base**.  
- **Mint rights do not expire, and transfer with a parent Natcat until utilized.**  
- The system operates **fully on-chain**, self-sustaining and **without centralized dependencies**.  

---

## Indexing
- The P2PPD on-chain index updates automatically and in perpetuity as new Natcats are inscribed.
- The index is published on-chain at:
  [`ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)  
- For instructions on how to query the Natcats on-chain index and/or generate a local copy, see [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md) (*see “How to Query Index” section*).  
- The on-chain index serves as the authoritative index moving forward, and functions as a hard fork of the previous Natcats index. The prior **TAP Protocol index** is valid up to block **919295**, and above this block is not authoritative.

---

## Minting
- New Natcats can be inscribed via inscription tools that provide full support for delegation and parent/child. 
- There is **no mint fee**, though platform service fees may apply.  
- Follow detailed instructions [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md#minting-instructions) to mint with the correct parameters and syntax.  

---

## Rendering
- **Generations 5+** render natively in Ordinals explorers by default once inscribed.  
- **Generations 1–4** render via the preexisting UNAT pathway (requires UNAT specific wallet support), but can optionally be **reinscribed** to enable native rendering.  
- Reinscriptions are **permanently packaged with the canonical inscription’s sat** and will travel together in perpetuity. Instructions can be found at [COMING SOON] 
<!-- - See [How to Enable Gen 1–4 Native Rendering](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md) for reinscription instructions.  --->

Examples  
- [Gen 1 UNAT Default Inscription](https://ordinals.com/inscription/5c26e644c0a93f02f964182fdab436378405d0f6639ca20134f747b160457e76i0)  
- [Gen 1 UNAT Native Render Inscription](https://ordinals.com/inscription/4d71c795bf62a1a458c5411b2b2ab0cb35209bb0ed7b5614a401ec781beadbbfi0)  

---

## Treasury
- Ten percent (10%) of new Natcats are allocated to a Natcats Treasury, to enable a combination of long term holding, partnerships, sales, and acquisitions in support of the project’s legacy.  

---

## Holder Action
- **No action is required** from holders.
