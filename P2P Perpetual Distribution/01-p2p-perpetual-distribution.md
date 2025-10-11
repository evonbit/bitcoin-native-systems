# Bitcoin-Native P2P Perpetual Distribution

## Introduction
Bitcoin-Native P2P Perpetual Distribution (“Perpetual Distribution”) is a model for the autonomous generation and distribution of non-fungible assets on Bitcoin Ordinals.

The model uses Bitcoin block data as an immutable generative data input to:
**(A)** dynamically issue asset supply, with one asset generated per eligible Bitcoin block,
**(B)** allocate new assets within a P2P network as a form of decentralized yield, and
**(C)** automatically index new assets as they are inscribed via an on-chain decentralized collection index.

Perpetual Distribution is a new [Digital Matter Theory](https://digital-matter-theory.gitbook.io/digital-matter-theory) (DMT) primitive that wraps the DMT Unique Non-Arbitrary Token (UNAT) framework and its required indexing functionalities in a fully on-chain system that does not require third-party protocol support. This enables decentralized production of Bitcoin-issued assets in perpetuity.

---

## Overview

---

## Architecture

### On-chain Supply Validation
**Purpose:** Determines asset supply based on emergent Bitcoin block data.

Asset supply for new non-fungible tokens is issued based on the occurrence of patterns in Bitcoin block data, with the potential to produce new assets dynamically over time.

Supply conditions are defined for a collection deployment via the deployment inscription (e.g., `bits contains "3b"`). The deployment inscription references the on-chain supply validator and validates new blocks as they are mined. Validation is performed on-chain using Ordinals recursive endpoints `/r/blockinfo/<QUERY>`. The validator authorizes production of one asset in a collection per validated Bitcoin block.

Once deployed on-chain, supply production is both generative and immutable, operating as long as new Bitcoin blocks are mined.

A finality buffer is enforced (e.g., 4 confirmations) to mitigate reorg risk prior to validation, meaning that new blocks will not be validated until N+4.

The on-chain supply validator is deployed in a shared module with the on-chain block-hash lottery.

### On-chain Block Hash Lottery
**Purpose:** Selects an authorized minter for each new asset via an on-chain lottery.

Mint rights for each new asset are allocated automatically to holders of assets in a pool, with pool winners selected via a block-hash lottery. The pool is built dynamically for each new asset, including all assets produced from lower block heights than the target asset (starting with an initial seed index of one or more assets).

Runs a deterministic block-hash-derived lottery to randomly select one asset from the pool, which becomes the "authorized parent."
- The holder of the authorized parent has exclusive rights to mint the new asset as a child of the authorized parent.
- New blocks are added to the pool as they are mined and become eligible to win for later block heights.

### On-chain Decentralized Indexing
**Purpose:** Maintains the on-chain index for a collection as new assets are inscribed.

Because new asset supply is issued dynamically and inscriptions by holders can occur at any time, a decentralized and dynamic indexer is required to maintain the latest canonical index for all assets. This index is tracked on-chain and updates automatically and in perpetuity as new assets are inscribed.

The on-chain index is produced from the outputs of the supply and lottery logics and is accessible via the deployment inscription for a collection.

The index returns:
- The canonical inscription ID for each Bitcoin block (via query).
- The results of the holder lottery for each Bitcoin block (via query).

Queries require a block height as an input and can be made for individual blocks via the interface available on-chain, or queried in bulk using the batch scripts.

### Deployment Inscription
**Purpose:** Deploy collection art and supply logics, and access the collection index.

The deployment inscription holds art generation logic and supply parameters for a collection, and provides on-chain access to the collection index.
- Sets parameters for art generated using Bitcoin block data as a generative seed.
- Sets collection supply parameters (e.g., `bits contains "3b"`).
- Routes asset inscriptions to Supply Validator, Block Hash Lottery, and Indexing logics.
- Provides access to the on-chain collection index.

### Asset Inscription
**Purpose:** Unique asset produced by a specific Bitcoin block.

Assets self-validate against the on-chain index and render natively in Ordinals explorers if they pass validation at runtime.

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

## Sample Deployment
The Perpetual Distribution deployment inscription for Natcats can be found here [`ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0) and recursively calls all Perpetual Distribution modules on-chain.

## Natcats Deployment of P2PPD
See [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/03-natcats-perpetual-distribution-upgrade.md) for information regarding the deployment of Perpetual Distribution for Natcats.

---
