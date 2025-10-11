# Bitcoin-Native P2P Perpetual Distribution

## Introduction
Bitcoin-Native P2P Perpetual Distribution (“Perpetual Distribution”) is a model for the autonomous generation and distribution of non-fungible assets on Bitcoin Ordinals.

The model uses Bitcoin block data as an immutable generative data input to:

- **(A)** dynamically issue asset supply, with one asset generated per eligible Bitcoin block  
- **(B)** allocate new assets within a P2P network as a form of decentralized yield  
- **(C)** automatically index new assets as they are inscribed via an on-chain decentralized collection indexer


Perpetual Distribution is a new [Digital Matter Theory](https://digital-matter-theory.gitbook.io/digital-matter-theory) (DMT) primitive that wraps the DMT Unique Non-Arbitrary Token (UNAT) framework and its required indexing functionalities in a fully on-chain system that does not require third-party protocol support. This enables decentralized production of Bitcoin-issued assets in perpetuity.

---


## Background

Perpetual Distribution builds on the **Digital Matter Theory Unique Non-Arbitrary Token (UNAT)** standard, pioneered by **Natcats** in February 2024.

The UNAT standard introduced generative artwork whose supply and rarity are determined by emergent Bitcoin block data. **P2P Perpetual Distribution** extends these foundations to enable sustainable and autonomous issuance of new supply.

Previous UNAT implementations included the following models and dependencies:

- **Open UNAT mints** – First-come claims by Bitcoin block ID. These were decentralized in principle but proved vulnerable to bots and unbalanced distribution in practice.  
- **Privileged-authorization UNAT mints** – A central authority issues supply. This model avoids bots successfully but introduces a centralized dependency. It is suitable for initial one-time distributions but cannot guarantee long-term issuance.  
- **Third-party indexers** – Both models rely on external indexers to track supply over time, which also cannot guarantee ongoing operation long term.

To ensure sustainable, autonomous issuance for collections such as **Natcats**, where supply may continue for decades, a system must support both decentralized issuance and balanced distribution controls. **P2P Perpetual Distribution** is designed to meet these requirements.

---



## System Overview

The Perpetual Distribution system consists of interconnected on-chain modules that autonomously generate, validate, and distribute new assets as Bitcoin blocks are mined.

### Components Summary

- **Supply Engine** – Validates Bitcoin blocks against supply conditions to authorize new supply.  
- **Allocation Engine** – Determines which existing asset holder receives authorization to mint the next asset.  
- **Decentralized Collection Indexing** – Maintains the canonical on-chain record of all assets within a collection, updating automatically as new assets are issued.  
- **Deployment Inscription** – Defines the collection’s generative logic, supply parameters, and routes asset inscriptions to the supply and allocation engines.  
- **Asset Inscription** – A unique non-fungible token asset associated with a specific Bitcoin block.  

---

## System Components

Below are detailed breakdowns of each component and their respective on-chain functions.


### Supply Engine


The on-chain supply engine validates Bitcoin blocks against collection-defined supply conditions ("patterns") to authorize new asset issuance. This enables dynamic, immutable, and perpetual asset generation as Bitcoin blocks are produced.

Supply conditions are defined in the deployment inscription (e.g., bits contains "3b"), and asset inscriptions route through it to validate against the supply engine. Each validated block authorizes the creation of one new asset within the collection.

Validation occurs on-chain through Ordinals recursive endpoints (`/r/blockinfo/<QUERY>`). A finality buffer (e.g., four confirmations) mitigates reorg risk by ensuring that blocks are not validated until block height +4.


### Allocation Engine


The on-chain allocation engine distributes mint rights for new asset supply as eligible Bitcoin blocks are produced. When a Bitcoin block generates a new asset, the block’s hash is used to deterministically select from a dynamic pool of all previously issued assets through an on-chain lottery.  

The selected asset becomes the **authorized parent** for the new asset, and only its holder is permitted to inscribe. Authorized parent validation is performed through a series of on-chain recursive calls, confirming that the inscribed asset is a direct child of the correct parent and the first valid child for that block height for that parent. Any other attempts are automatically rejected by the on-chain validator and excluded from indexing.  

As new supply is inscribed, it is added to the on-chain index, expanding the pool for subsequent lotteries. Newly issued assets immediately become eligible to win future blocks.


### Decentralized Collection Indexing

As new supply is inscribed, it is automatically indexed by a decentralized on-chain collection index. This maintains the canonical index of assets in perpetuity. The index is derived from the outputs of the supply validation and allocation modules and is accessible through the deployment inscription for each collection.

The index provides:
- The canonical inscription ID for each Bitcoin block  
- The authorized parent and holder lottery results for each block  

Queries require a block height as input and can be executed directly through the on-chain interface or in batch using the provided scripts.


### Deployment Inscription

The deployment inscription contains the foundational parameters and logic for a collection, including art generation, supply conditions, and references to the on-chain modules responsible for validation, allocation, and indexing. Once deployed, it serves as the canonical access point for the collection’s on-chain state and index.

It performs the following functions:
- Defines parameters for art generation using Bitcoin block data as a generative seed  
- Sets collection supply conditions (e.g., `bits contains "3b"`)  
- Routes asset inscriptions to the Supply Validation, Allocation, and Indexing modules  
- Provides on-chain access to the collection index



### Asset Inscription

Each asset inscription self-validates against the on-chain index and renders natively in Ordinals explorers if it passes validation at runtime. 

The block number that produced the asset is encoded within the asset inscription’s undelegated content (see [Mint Instructions](#mint-instructions)), and delegates to the collection deployment inscription.




---

## Sample Deployment
An example deployment inscription can be found here [`ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0) and recursively calls the supply and allocation engines. 

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

## Natcats Deployment of P2PPD
See [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/03-natcats-perpetual-distribution-upgrade.md) for information regarding the deployment of Perpetual Distribution for Natcats.

---
