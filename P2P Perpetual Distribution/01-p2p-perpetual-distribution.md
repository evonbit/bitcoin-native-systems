# Bitcoin-Native P2P Perpetual Distribution

## Introduction
Bitcoin-Native P2P Perpetual Distribution (“Perpetual Distribution”) is a model for the autonomous generation and distribution of non-fungible assets on Bitcoin Ordinals.

The model uses Bitcoin block data as an immutable generative data input to:

- **(A)** dynamically issue asset supply, with one asset generated per eligible Bitcoin block  
- **(B)** allocate new assets within a P2P network as a form of decentralized yield  
- **(C)** automatically index new assets as they are inscribed via an on-chain decentralized collection index


Perpetual Distribution is a new [Digital Matter Theory](https://digital-matter-theory.gitbook.io/digital-matter-theory) (DMT) primitive that wraps the DMT Unique Non-Arbitrary Token (UNAT) framework and its required indexing functionalities in a fully on-chain system that does not require third-party protocol support. This enables decentralized production of Bitcoin-issued assets in perpetuity.

---

## System Overview

### On-chain Supply Validation

### Purpose
Determines asset supply based on emergent Bitcoin block data.

### Description
The on-chain supply validation system issues new non-fungible tokens based on patterns in Bitcoin block data, enabling dynamic and perpetual asset generation as Bitcoin blocks are produced. Supply conditions for a collection are defined in the deployment inscription (e.g., bits contains "3b"), which references the on-chain validator to verify new blocks as they are mined. Once deployed, supply production is generative, immutable, and continues autonomously for as long as new Bitcoin blocks are produced.

Validation occurs entirely on-chain through Ordinals recursive endpoints (`/r/blockinfo/<QUERY>`). Each validated block authorizes the production of one new asset within the collection. A finality buffer (e.g., four confirmations) mitigates reorg risk by ensuring that blocks are not validated until block height +4.


### On-chain Allocation
**Purpose:** Allocates mint rights for each new asset to a specific asset holder.

The on-chain allocation system distributes mint rights for new asset supply as eligible Bitcoin blocks are produced. When a Bitcoin block generates a new asset, the block’s hash is used to deterministically select from a dynamic pool of all previously issued assets through an on-chain lottery.  

The selected asset becomes the **authorized parent** for the new asset, and only its holder is permitted to inscribe. Authorized parent validation is performed through a series of on-chain recursive calls, confirming that the inscribed asset is a direct child of the correct parent and the first valid child for that block for that parent. Any other attempts are automatically rejected by the on-chain validator and excluded from indexing.  

As new supply is inscribed, it is added to the on-chain index, expanding the pool for subsequent lotteries. Newly issued assets immediately become eligible to win future blocks, ensuring continuous, decentralized allocation over time.

### On-chain Decentralized Indexing
**Purpose:** Maintains the on-chain index for a collection as new assets are inscribed.

The on-chain indexing system continuously records and verifies all assets within a collection. Because new supply is issued dynamically and inscriptions can occur at any time, the indexer operates in a fully decentralized and self-updating manner. It maintains the canonical state of the collection directly on-chain, updating automatically and in perpetuity as new assets are created.  

The index is generated from the outputs of the supply validation and allocation modules and is accessible through the deployment inscription for each collection. It returns:  
- The canonical inscription ID for each Bitcoin block.  
- The results of the holder lottery for each Bitcoin block.  

Queries require a block height as input and can be executed individually through the on-chain interface or in bulk using the provided batch scripts.


### Deployment Inscription
**Purpose:** Defines the generative art and supply logic for a collection, and serves as the access point for its on-chain index.

The deployment inscription establishes the foundational parameters and routing for a collection. It contains the art generation logic, supply conditions, and references to the on-chain modules responsible for validation, allocation, and indexing. Once deployed, it acts as the canonical access point for the collection’s on-chain state and index.  

It performs the following functions:  
- Defines parameters for art generation using Bitcoin block data as a generative seed.  
- Sets collection supply conditions (e.g., `bits contains "3b"`).  
- Routes asset inscriptions to the Supply Validation, Allocation, and Indexing modules.  
- Provides on-chain access to the collection index.

## Asset Inscription

### Purpose
A unique asset produced by a specific Bitcoin block.

### Description
Each asset inscription self-validates against the on-chain index and renders natively in Ordinals explorers if it passes validation at runtime. The block number that produced the asset is encoded within the asset inscription’s undelegated content (see [Mint Instructions](#mint-instructions)). During validation, the asset inscription delegates to its deployment inscription, which handles routing and execution to relevant modules and subsystems, ensuring the asset remains deterministically linked to its originating block and verifiable against protocol-defined validation rules.


---

## Sample Deployment
An example deployment inscription can be found here [`ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0) and recursively calls all other modules on-chain. 

---

## Minting Instructions
To inscribe a new asset issued via Perpetual Distribution:

1. **Check the authorized block winner**
   - At **block height +4** (confirmation buffer), the lottery winner for an eligible Bitcoin block becomes available.
   - To determine the winner, you can either:
     - Query a single block via the deployment inscription in Ordinals explorer using the *Authorization* input field, or
     - Run the [Authorization Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/02-scripts/authorization-script.py) to construct a local index for all blocks or a specified range.
   - The query will return the **winning block number**. The valid asset associated with this block number is the **authorized parent** for the new asset.

2. **If you hold the authorized parent**
   - Inscribe the new asset according to the following requirements:
     - Inscription is a **child of the authorized parent inscription**.
     - Inscription **delegates to the collection deployment inscription ID**.
     - Inscription’s undelegated content includes the following JSON with the correct block and ticker reference, for example:
       ```json
       {"blk": 999999, "tick": "natcats"}
       ```
       Replace `999999` with the target block number for the new asset, and `tick` with the relevant collection ticker.  
       **Note:** The ticker is case-sensitive.
   - Assets can be inscribed using any tool with full support for **Ordinals Protocol v2.2.1 or later**.

3. **Validation**
   - To pass validations, inscriptions must meet the above requirements and be the first inscription to do so.
   - Any inscription that fails to meet these requirements or is not first will not render and will be automatically rejected by the indexer.

---

## How to Query On-chain Index
To query the collection index and find the canonical ID for a given asset, you can either:
- Query for a Bitcoin block number via the deployment inscription in Ordinals explorer using the *Index* input field. This will produce the ID for its associated asset.
- Run the [Indexing Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/02-scripts/index-script.py) to construct a local index of assets associated with all blocks or a specified range.

---

## Background: DMT UNAT
Perpetual Distribution builds on the **Digital Matter Theory Unique Non-Arbitrary Token (UNAT) standard**, pioneered by Natcats in February 2024.

The UNAT standard introduced the concept of generative artwork with asset supply governed by emergent Bitcoin block data. P2P Perpetual Distribution builds on these foundations while addressing limitations regarding sustainable issuance of new supply:
- **Open UNAT mints** (first-come claims by Bitcoin block ID) were decentralized in principle but, in practice, proved vulnerable to bots and unbalanced allocation.
- **Privileged authorization UNAT mints** (a central authority issues supply) avoid bots successfully but introduce a centralized dependency. This is suitable for initial one-time mint distribution but cannot guarantee issuance long-term.
- In both cases, **third-party indexers** are required to track supply over time, which cannot guarantee long-term operation.

To ensure the long-term issuance of collections such as Natcats (where supply has the potential to be produced autonomously over decades), it is necessary to support both **decentralized issuance** and **balanced distribution controls**. This is provided by P2P Perpetual Distribution.

---

## Natcats Deployment of P2PPD
See [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/03-natcats-perpetual-distribution-upgrade.md) for information regarding the deployment of Perpetual Distribution for Natcats.

---
