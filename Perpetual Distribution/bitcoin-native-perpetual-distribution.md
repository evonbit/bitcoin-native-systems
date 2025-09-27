# Bitcoin-Native Perpetual Distribution  

## Introduction  
Bitcoin-Native Perpetual Distribution (“Perpetual Distribution”) is a model for the autonomous generation and distribution of non-fungible assets on Bitcoin Ordinals.  

The model uses Bitcoin block data as an immutable generative input to:  
(A) dynamically issue asset supply, one per eligible Bitcoin block, and  
(B) allocate new assets within a P2P network as a yield.  

Perpetual Distribution is a new Digital Matter Theory primitive, which wraps the Unique Non-Arbitrary Token (UNAT) framework and indexing functionalities in a fully on-chain system that does not require third-party protocol or indexing dependencies. This enables decentralized production of Bitcoin-issued assets in perpetuity.  

---

## Overview  
- **Generative supply** — Asset supply is issued based on occurrence of patterns in Bitcoin block data, producing new assets dynamically over time.  
- **P2P yield for holders** — Mint rights for each new asset are allocated automatically to a holder of a prior asset, selected via a block-hash lottery.  
- **Decentralized indexing** — An on-chain collection index updates automatically as new assets are produced, maintaining the canonical record of assets.  
- **Native rendering & validation** — Assets validate against the on-chain index and render natively in Ordinals explorers.  

---

## Architecture  

### Supply Validation  
**Purpose:** Determines which Bitcoin blocks are eligible to generate new assets.  
**Core Functions**  
- Validates eligible Bitcoin blocks against specific patterns (e.g., bits contains “3b”, block height contains “69”) via recursion.  
- Authorizes production of one asset in a collection per validated Bitcoin block.  
- Enforces a finality buffer (e.g., 4 confirmations) to mitigate reorg risk prior to validation.  

### Hash Lottery  
**Purpose:** Selects an authorized minter for each new asset via on-chain lottery.  
**Core Functions**  
- Builds pool of assets in the collection that are eligible to win mint rights (all assets produced from a Bitcoin block earlier than the block for the new asset).  
- Runs deterministic block-hash-derived lottery to select one asset from the pool.  
- Authorizes the holder of this asset with exclusive rights to mint for a given block number.  
- *Note:* Pool requires an initial seed index of one or more assets.  

### Decentralized Indexer  
**Purpose:** Maintains the canonical index of valid mints on-chain as new assets are inscribed.  
**Core Functions**  
- Returns the canonical inscription ID for each Bitcoin block, via query.  
- Returns the results of the holder lottery for each Bitcoin block, via query.  
- *Note:* The indexer is queried via deployment inscription.  

### Asset Inscription  
**Purpose:** Unique asset produced by a specific Bitcoin block.  
**Core Functions**  
- Validates against the decentralized indexer and renders content only if the asset meets validation criteria (see *Minting Instructions*).  

### Deployment Inscription  
**Purpose:** Holds art generation logic and supply parameters for a collection, and provides on-chain access to the collection index.  
**Core Functions**  
- Produces art generated using Bitcoin block data as a generative seed.  
- Sets collection parameters including supply pattern (e.g., bits contains 3b, min/max block height).  
- Routes asset inscriptions to Supply Validation and Hash Lottery logic.  
- Provides access to decentralized indexer queries via Ordinals explorer.  

---

## Minting Instructions  
To mint a new asset issued via Perpetual Distribution:  

1. **Check the authorized block winner**  
   - At **block height +4** (confirmation buffer), the lottery winner becomes available.  
   - To determine the winner, you can either:  
     - Query a single block via an **Ordinals Explorer** using the *Authorization* input field, or  
     - Run a script to construct a **local index** for all blocks or a specified range.  
   - The query will return the **winning block number**. The valid asset associated with this block number is the **authorized parent** for the new asset.  

2. **If you hold the authorized block winner**  
   - Inscribe the new asset, ensuring the following requirements are met:  
     - The inscription is a **child of the authorized block winner inscription**.  
     - The inscription **delegates to the collection deployment inscription ID**.  
     - The undelegated content includes the following JSON with the correct block and ticker reference, for example:  
       ```json
       {"blk": 999999, "tick": "natcats"}
       ```  
       Replace `999999` with the target block number.  
       **Note:** The ticker is case sensitive.  
   - Assets can be inscribed using any tool that supports **Ordinals protocol v2.2.1 or later**.  

3. **Validation rules**  
   - Any inscription that fails these requirements will not render and will be automatically rejected by the index.  
   - Only the **first valid asset** meeting these requirements will index and render.  

---

## Index Query Instructions  
To produce or query the canonical collection index:  
- Visit the collection deployment inscription.  
- To retrieve results, you can either:  
  - Query a single block via an Ordinals Explorer, or  
  - Run a script to construct a local index covering all blocks or a specified range.  

---

## Background: DMT UNAT  
Perpetual Distribution builds on the **DMT UNAT standard**, pioneered by Natcats in February 2024. [Link](https://digital-matter-theory.gitbook.io/digital-matter-theory)  

The UNAT standard introduced the concept of **generative artwork with asset supply governed directly by Bitcoin block data**. Perpetual Distribution builds on these foundations while addressing limitations around the **sustainable issuance of new supply**.  

- **Open mints** (first-come claims by Bitcoin block ID) were decentralized in principle, but in practice proved vulnerable to bots and unbalanced allocation.  
- **Privileged authorization mints** (a central authority issues supply) avoided bots but introduced a **centralized dependency**, preventing guaranteed long-term issuance.  
- In both cases, **third-party indexers** were required to track supply over time — a dependency that cannot guarantee **long-term operation**.  

To ensure the long-term issuance of collections such as Natcats (where supply is produced autonomously over decades), it is necessary to enable both **decentralized issuance** and **balanced distribution controls**. Perpetual Distribution provides this by wrapping all logic and indexing in an on-chain system that requires no metaprotocol support.  

---

## Natcats Deployment  
See [here] for information regarding the deployment of Perpetual Distribution for Natcats.  

---

## Demo  
Demo can be found [here].  
