# Bitcoin-Native P2P Perpetual Distribution  
*A fully on-chain system for perpetual decentralized asset issuance on Bitcoin Ordinals.*

## Introduction
**Bitcoin-Native P2P Perpetual Distribution (“Perpetual Distribution”)** is a model for the autonomous generation and distribution of non-fungible assets on Bitcoin Ordinals.

The model uses Bitcoin block data as an immutable generative data input to:

- **(A)** Dynamically issue asset supply, with one asset generated per eligible Bitcoin block  
- **(B)** Allocate new assets within a P2P network as a form of decentralized yield  
- **(C)** Automatically index new assets as they are inscribed via an on-chain decentralized collection indexer  

This enables decentralized production of Bitcoin-issued assets in perpetuity, without third-party protocol support.

---

## Core Functionalities

### 1. Supply Generation
Collection supply is dynamic and controlled by the Bitcoin blockchain’s immutable data, which functions as a generative input governing asset issuance.  
Each asset corresponds to a specific Bitcoin block.  

Each block is validated against the collection’s supply condition using Bitcoin Core to determine eligibility (for example, `bits contains "3b"`).  
When a block meets this condition, it authorizes the creation of one new asset.  

Validation occurs directly on-chain via recursive calls, and new supply becomes eligible after +4 confirmations to account for potential chain reorganizations.

---

### 2. Allocation & Distribution
When a Bitcoin block meets the supply condition, the **Distribution Engine** deterministically selects an existing asset *in the collection* as the **authorized parent**, using the block hash as a deterministic random seed.  
Only the holder of that parent may inscribe the new asset; unauthorized inscriptions are automatically rejected from indexing.  

Mint rights:
- Are allocated automatically  
- Transfer with the parent asset  
- Never expire  
- Are validated through the on-chain recursive system  

Each newly inscribed asset immediately joins the asset pool and becomes eligible to win assets for future blocks.

---

### 3. Indexing & Discovery
Each new inscription updates the on-chain collection index, which maintains the canonical record of:
- The Bitcoin block that produced the asset  
- The authorized parent  
- The resulting asset inscription ID  

The index is fully autonomous and accessible via the Deployment Inscription or through provided scripts:
- [Indexing Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/02-scripts/index-script.py) — builds a local index of all or specific block ranges  
- [Authorization Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/02-scripts/authorization-script.py) — identifies authorized parents and allocation results  

This makes it possible for anyone to verify allocation results, share them with the community, or integrate the data into marketplaces and analytical tools.

---

### 4. Validation & Rendering
All inscriptions are validated through recursive on-chain checks against the Distribution Engine.  
Assets will only render if they meet these validation rules, and valid inscriptions are added to the canonical collection index.

Validation rules ensure:
- The block meets the defined supply condition  
- The parent is the correct authorized winner  
- No prior valid child exists for that block  

The asset for a specific block cannot be duplicated — only the first valid, correctly structured inscription is recognized and rendered on-chain.  
Invalid or duplicate inscriptions are not indexed and will not render.

---

## Architecture Overview
P2P Perpetual Distribution operates through a network of on-chain inscriptions connected via recursive calls and delegation.

- **Deployment Inscription** — Defines the collection’s parameters and generative art. Performs recursive calls to the Distribution Engine Inscription and serves as the canonical access point.  
- **Distribution Engine Inscription** — Contains:  
  - **Supply Module** — Validates Bitcoin blocks against collection conditions, with calls to Bitcoin Core via Ordinals recursive endpoints.  
  - **Allocation Module** — Determines authorized parent assets via deterministic selection.  
- **Index Access Point** — Returns the authorized parent and canonical asset ID for each block, accessed via the Deployment Inscription.  
- **Asset Inscriptions** — Each individual asset inscription represents a unique asset within the collection. It delegates to the Deployment Inscription, which routes to other modules.

---

### Architecture Diagram

