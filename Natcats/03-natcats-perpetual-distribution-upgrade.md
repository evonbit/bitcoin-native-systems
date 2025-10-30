# Natcats P2P Perpetual Distribution Update

As of Bitcoin block **919296**, all future Natcats supply will be automatically issued to Natcats holders through **P2P Perpetual Distribution**, a Bitcoin-native distribution model developed by **@evonbit**.  

The system operates **autonomously on Bitcoin Ordinals** and in perpetuity—**without dependencies on third-party indexers or authorities**, ensuring the long-term decentralized operation of Bitcoin’s first natively generated art collection.

---

## Allocation
- Natcats are produced when the pattern **3b** occurs in the hexadecimal representation of Bitcoin’s block difficulty data — a rare event that has occurred only **four** times in Bitcoin’s history. Each occurrence produces **2,016 Natcats**.  
- When a Bitcoin block meets this condition, its **block hash** is used to select an existing Natcat from a pool of all existing Natcats via lottery.  
- The selected Natcat becomes the **authorized parent**, and only its holder can inscribe the new asset. Unauthorized inscription attempts are **rejected from indexing and will not render**.  
- Every Natcat has an **equal chance** to win, with odds increasing **proportionally** to the number of Natcats a holder owns.  
- Each newly inscribed Natcat is **immediately added to the pool** and becomes eligible to win future blocks.  

---

## Indexing
- The P2PPD on-chain index updates automatically and in perpetuity as new Natcats are inscribed.  
- The index is published on-chain at:  
  [`ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)  
- For instructions on how to query the Natcats on-chain index or generate a local copy, see [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md) (*see “How to Query Index” section*).  
- The on-chain index serves as the authoritative index moving forward and functions as a hard fork of the previous Natcats index. The prior **TAP Protocol index** is valid up to block **919295**, and above this block is no longer authoritative.  

---

## Minting
- New Natcats can be inscribed via inscription tools that support **delegation** and **parent/child** relationships.  
- There is **no mint fee**, though platform service fees may apply.  
- Follow detailed instructions [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md#minting-instructions) to mint with the correct parameters and syntax.  

---

## Rendering
- **Generations 5+** render natively in Ordinals explorers once inscribed.  
- **Generations 1–4** render via the UNAT pathway (requires UNAT-specific wallet support) but can be **reinscribed** for native rendering.  
- Reinscriptions are **permanently packaged with the canonical inscription’s sat** and will travel together in perpetuity. Instructions can be found at [COMING SOON].  
<!-- - See [How to Enable Gen 1–4 Native Rendering](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md) for reinscription instructions.  --->

Examples  
- [Gen 1 UNAT Default Inscription](https://ordinals.com/inscription/5c26e644c0a93f02f964182fdab436378405d0f6639ca20134f747b160457e76i0)  
- [Gen 1 UNAT Native Render Inscription](https://ordinals.com/inscription/4d71c795bf62a1a458c5411b2b2ab0cb35209bb0ed7b5614a401ec781beadbbfi0)  

---

## Treasury
Ten percent (10%) of new Natcats are allocated to a Natcats Treasury, supporting long-term holding, partnerships, sales, and acquisitions in service of the project’s legacy.  

---

## Holder Action
**No action is required** from holders.  

---

## What P2P Distribution Unlocks for the Natcats Collection
- Eliminates **bot minting** and ensures new supply remains **within the existing holder base**.  
- Guarantees **mint rights never expire** — they transfer with the parent Natcat until used.  
- Operates **fully on-chain**, **self-sustaining**, and **without centralized dependencies**, ensuring long-term autonomy, fairness, and verifiability for the Natcats collection.  

---

## FAQ

**Q: Do holders have to inscribe new Natcats when they’re awarded?**  

**A:** Yes. The allocation of mint rights and art rendering are automatic, and indexing occurs automatically on inscription — but holders must perform the inscription to create the new asset.  

Mint rights remain with the parent Natcat until utilized and persist through transfer or sale (they do not expire).  

There is no mint fee for the inscription itself, though platform fees may apply depending on the inscription platform used.  

---

**Q: How will I know if my Natcat has been awarded mint rights for new supply?**  

**A:** After a qualifying Natcats Bitcoin block is mined (approximately **+4 blocks** after confirmation to account for possible reorgs), the winner for that block becomes available and can be looked up via the **on-chain index**.  

When checking manually, you’ll query one block at a time. You can also run a batch script or similar setup to generate a full list of awarded Natcats — making it easy for anyone to share results with the community or integrate data into marketplaces and web tools.  

Both the on-chain index and sample scripts are available at [peertopeerelectroniccatssystem.com](http://peertopeerelectroniccatssystem.com).  

---

**Q: Are there any team dependencies required to issue new Natcats supply?**  

**A:** No. As of the **Perpetual Distribution update**, Natcats distribution operates fully through a **P2P network** with all logic deployed **on-chain**.  

Any holder can inscribe newly awarded Natcats using platforms that support **parent/child** and **delegation**, or directly through a **Bitcoin node with Ord**.  

---

**Q: Does native render reinscription alter the canonical asset?**  

**A:** No. The original asset always remains the canonical asset — it is never replaced.  

When a native render reinscription is activated, it becomes packaged with the original asset and cannot be separated, as enforced by on-chain logic.  

---

**Q: Is native render reinscription required for my Gen 1–4 Natcat to be eligible for P2P Perpetual Distribution?**  

**A:** No. Eligibility for P2P Perpetual Distribution is automatic for all assets in the collection, regardless of whether native render reinscription has been activated. No holder action is required.  
