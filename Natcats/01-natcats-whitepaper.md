# Natcats: A Peer-to-Peer Electronic Cats System  
evonbit  
[@dmtnatcats](https://x.com/dmtnatcats)  

---

## Abstract  
Natcats are collectible digital cats produced by the Bitcoin blockchain. Natcats are produced when specific data properties occur within Bitcoin blocks, with the data for each block determining each cat’s unique traits. All Natcats systems are deployed fully on-chain on Bitcoin Ordinals, enabling autonomous production for up to 150+ years. New cats are distributed automatically to Natcats holders.  

---

## Introduction  
The Bitcoin blockchain produces a continuous sequence of blocks, each containing unique and immutable data. Natcats transforms this data into an autonomously generating art collection, with rarities and supply production determined by Bitcoin itself, without reliance on centralized entities.  

Created by **evonbit** and launched in February 2024 as a free mint via Bitcoin Ordinals, Natcats is the first art collection to be generated natively by the Bitcoin blockchain.  

---

## Supply Mechanism  

### 2.1 Bits & the “3b” Pattern  
Each Bitcoin block contains a **Bits** value in its header, which represents the network’s difficulty at the time of mining. The value is recalculated every **2,016 blocks** (roughly every two weeks) to maintain a consistent pace of block production.  

A Natcat is produced when the hexadecimal representation of a block’s Bits value contains the substring **“3b.”** This event is rare; as of this writing, it has occurred in only four difficulty periods, each producing a distinct generation of 2,016 Natcats — 8,064 in total across 900k+ blocks mined to date.  

### 2.2 Dynamic Supply  
Because the Bits value changes according to Bitcoin’s mining difficulty, new supply is unpredictable. The next generation of Natcats might appear within a year, after fifty years, or never again.  

---

## Trait Generation  
Each Natcat’s traits are determined by the data properties of its block number. For example:  

- If the block number ends in the digit **7**, the Natcat will have a green face.  
- If the block number contains **420**, the Natcat will have the trait *catnip cig*.  
- If the block number is a multiple of **69**, the Natcat will have the trait *spikes collar*.  

Because supply is not fixed, trait rarity is dynamic. Traits with zero current occurrence may be released for the first time far in the future, while others may become proportionally rarer as new blocks are mined.  

See the full [Natcats Traits List](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/02-natcats-traits.md) for details.  

---

## Minting Natcats  

### 4.1 Eligibility  
- **Generations 1–4**: Natcats in these generations were made available through open mint to the public, with no ownership prerequisites.  
- **Generations 5 and beyond**: Mint rights for new Natcats are automatically allocated to existing holders via P2P Perpetual Distribution.  

### 4.2 Perpetual Distribution  
An on-chain P2P Perpetual Distribution system automatically allocates mint rights for each new Natcat via a block-hash lottery among existing holders.  

When a Bitcoin block containing the “3b” property is mined, the block’s hash is used as a deterministic seed to select a prior block from the set of earlier “3b” blocks. The Natcat associated with the winning block becomes the **authorized parent** for the new cat. Only this holder can inscribe the new Natcat. Other attempts will not render and are automatically rejected from indexing.  

Mints have no expiry, require no central coordination, and can be made using any inscription tool that provides full support for **Ordinals protocol v2.2.1 or later**. Ten percent (10%) of new Natcats are allocated to a Natcats Treasury, to enable a combination of long term holding, partnerships, sales, and acquisitions in support of the project’s legacy.  

[Perpetual Distribution documentation](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/01-p2p-perpetual-distribution.md)  

### 4.3 Decentralized Indexing  
Natcats are indexed automatically via an on-chain decentralized indexer as they are produced, published on-chain at inscription [765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)

Querying this indexer returns the canonical inscription ID and authorized block winner for each cat, updating automatically and in perpetuity as new cats are produced and inscribed by holders. Run [these scripts](https://github.com/evonbit/bitcoin-native-systems/tree/main/P2P%20Perpetual%20Distribution/02-scripts) to generate a complete local copy of either dataset from the on-chain index. 

---

## Deployment  

### 5.1 Deployment History  
On its launch in February 2024, Natcats pioneered the Digital Matter Theory **Unique Non-Arbitrary Token (UNAT)** standard. In October 2025, Natcats enabled **P2P Perpetual Distribution** and native rendering, to support full decentralization of distribution, indexing, and rendering for the UNAT framework.  

### 5.2 Rendering Paths  
The first four generations of Natcats render via the UNAT standard default render pathway, which requires UNAT-specific wallet support to display on-chain artwork. Gen 1–4 Natcats can optionally be **reinscribed** to enable native rendering, which renders natively in Ordinals explorers with full support for Ordinals version 2.2.1 or later. Reinscription instructions can be found at [COMING SOON].  

<!-- See [How to Enable Native Render Reinscription](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md) for detailed native render reinscription instructions.   --->

Generations **5 and beyond** use native rendering by default.  

Examples  
- [Gen 1 UNAT Default Inscription](https://ordinals.com/inscription/5c26e644c0a93f02f964182fdab436378405d0f6639ca20134f747b160457e76i0)  
- [Gen 1 UNAT Native Render Inscription](https://ordinals.com/inscription/4d71c795bf62a1a458c5411b2b2ab0cb35209bb0ed7b5614a401ec781beadbbfi0)  

---

## Links  

### Project Links  
- [X](https://x.com/dmtnatcats)  
- [Magic Eden Marketplace](https://magiceden.io/ordinals/marketplace/dmtnatcats)  
- [Discord](https://discord.gg/PaQPwWXUSz)  
- [GitHub](https://github.com/evonbit)  
- [Viewer (View cats + download image file)](https://peertopeerelectroniccatssystem.com/cats/)  

### Related Links  
- [Ordinals Documentation](https://docs.ordinals.com/)  
- [Digital Matter Theory](https://digital-matter-theory.gitbook.io/digital-matter-theory)  
