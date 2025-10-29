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
Collection supply is dynamic and controlled by the Bitcoin blockchain’s immutable data, which functions as a generative input governing asset issuance. Each asset corresponds to a specific Bitcoin block.  

Each block is validated against the a supply condition for the collection (for example, `block's bits field contains "3b"`)  against Bitcoin Core to determine eligibility. When a block meets this condition, it authorizes the creation of one new asset.  

Validation occurs directly on-chain via recursive calls, and new supply becomes eligible after +4 confirmations to account for potential chain reorganizations.

---

### 2. Allocation & Distribution
When a Bitcoin block meets the supply condition (e.g. `bits contains "3b"`), the **Distribution Engine** deterministically selects an existing asset *in the collection* as the **authorized parent**, using the Bitcoin block’s hash as a deterministic random seed. Only the holder of that parent may inscribe the new asset; unauthorized inscriptions are automatically rejected from indexing.  

Mint rights:
- Are allocated automatically  
- Transfer with the parent asset  
- Never expire  
- Are validated through the on-chain recursive system  

Each newly inscribed asset immediately joins the asset pool and becomes eligible to win assets for future blocks.  

The system begins with a seed index of one or more assets, forming the first eligible pool for allocation.  
From this starting pool, new assets are issued and added automatically, creating a self-sustaining distribution cycle on-chain.

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
All inscriptions are validated through recursive on-chain checks against the Distribution Engine. Assets will only render if they meet these validation rules.  

Validation rules ensure:
- The block meets the defined supply condition  
- The parent is the correct authorized winner  
- No prior valid child exists for that block  

The asset for a specific block cannot be duplicated — only the first valid, correctly structured inscription is recognized and rendered on-chain. Invalid or duplicate inscriptions are not indexed and will not render.

---

## Architecture Overview
P2P Perpetual Distribution operates through a network of on-chain inscriptions connected via recursive calls and delegation.

- **Deployment Inscription** — Defines the collection’s parameters and generative art. Performs recursive calls to the Distribution Engine Inscription and serves as the canonical access point.  
- **Distribution Engine Inscription** — Contains:  
  - **Supply Module** — Validates Bitcoin blocks against collection conditions, with calls to Bitcoin Core via Ordinals recursive endpoints.  
  - **Allocation Module** — Determines authorized parent assets via deterministic selection.  
- **Index Access Point** — Returns the authorized parent and canonical asset ID for each block, accessed via the Deployment Inscription.  
- **Asset Inscriptions** — Each individual asset inscription represents a unique asset within the collection. Delegates to the Deployment Inscription, which routes to other modules.

---

### Architecture Diagram

             ┌──────────────────────────────┐
             │       Asset Inscription      │
             └──────────────────────────────┘
                            ▲
                            │
             ┌──────────────────────────────┐──────────────┐
             │     Deployment Inscription   │              │
             └──────────────────────────────┘              │
                            ▲                              │
                            │                              ▼
             ┌──────────────────────────────┐   ┌──────────────────────┐
             │  Dist. Engine Inscription    │──▶│  Index Access Point  │
             │  ├─ Supply Module            │   └──────────────────────┘
             │  └─ Allocation Module        │
             └──────────────────────────────┘


---

## How to Interact with P2P Perpetual Distribution

Collection holders and developers interact with P2PPD in the following way to verify allocations, inscribe new assets, and monitor ongoing distribution.

### 1. Allocation of Mint Rights
When a qualifying Bitcoin block is mined, P2PPD automatically allocates mint rights to an existing holder through the on-chain allocation process.  
Allocation of mint rights and indexing are both automatic. However, holders must take the action to inscribe the new asset (see [3. Inscribing New Assets](#3-inscribing-new-assets)).

Mint rights remain attached to the authorized parent until used and persist through transfers or sales without expiry.

---

### 2. Checking for New Allocations
After an eligible Bitcoin block is mined and confirmed (+4 blocks), allocation results become visible through the on-chain index.  
Holders can check whether their asset was selected as follows:

- Manual query via the Deployment Inscription using the *Authorization* input field  
- Batch lookup using the [Authorization Script](https://github.com/evonbit/bitcoin-native-systems/tree/main/P2P%20Perpetual%20Distribution/02-scripts) to generate a local list of all awarded assets  

This allows for transparent verification and open sharing of new allocation data.

---

### 3. Inscribing New Assets
If you hold the authorized parent, inscribe the newly awarded asset following the [Minting Instructions](#minting-instructions) below.  
All validation, rendering, and indexing occur fully on-chain — no team involvement or centralized infrastructure is required.

---

## Minting Instructions
To inscribe a new asset generated by P2PPD:

1. **Check the Authorized Block Winner**  
   - After block height +4, visit the Deployment Inscription or use the [Authorization Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/02-scripts/authorization-script.py) to confirm the winning parent.

2. **If You Hold the Authorized Parent**  
   - Inscribe as a child of the authorized parent  
   - Delegate to the collection’s Deployment Inscription ID  
   - Include undelegated JSON content:
     ```json
     {"blk": 999999, "tick": "collectionticker"}
     ```
     Replace `999999` with the correct block number and `collectionticker` with the case-sensitive collection ticker (e.g. `"natcats"`).

3. **Validation**
   - Only the first valid inscription per block and parent renders.  
   - Invalid or duplicate inscriptions will not render or appear in the on-chain index.

---

## How to Query the On-Chain Index
You can query the canonical collection index in two ways:
- Manual Query — via the Deployment Inscription’s *Index* input field by specifying a Bitcoin block number.  
- Local Index Generation — using the [Indexing Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/P2P%20Perpetual%20Distribution/02-scripts/index-script.py) to build a complete or partial index dataset.

---

## Sample Deployment
An example deployment inscription (**Natcats**) can be found at  
[`ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0`](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0).  

This deployment inscription recursively calls the other on-chain modules.


---

## Background
Perpetual Distribution is a new **Digital Matter Theory (DMT)** primitive that wraps the DMT **Unique Non-Arbitrary Token (UNAT)** framework and its required indexing functionalities in a fully on-chain system that does not require third-party protocol support.

The UNAT standard, pioneered by **Natcats** in February 2024, introduced generative artwork whose supply and rarity are determined by emergent Bitcoin block data.  

Previous UNAT implementations included the following models and dependencies:  
- **Open UNAT mints** – First-come claims by Bitcoin block ID. These were decentralized in principle but proved vulnerable to bots and unbalanced distribution in practice.  
- **Privileged-authorization UNAT mints** – A central authority issues supply. This model avoids bots successfully but introduces a centralized dependency. It is suitable for initial one-time distributions but cannot guarantee long-term issuance.  
- **Third-party indexers** – Both models rely on external indexers to track supply over time, which also cannot guarantee ongoing operation long term.  

To ensure sustainable, autonomous issuance for collections such as **Natcats**, where supply may continue for decades, a system must support both decentralized issuance and balanced distribution controls.  
**P2P Perpetual Distribution** is designed to meet these requirements.

---

## Resources
- [GitHub Repository](https://github.com/evonbit/bitcoin-native-systems)  
- [peertopeerelectroniccatssystem.com](http://peertopeerelectroniccatssystem.com)  

---

## Natcats Deployment of P2PPD
See [here](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/03-natcats-perpetual-distribution-upgrade.md) for information regarding the deployment of Perpetual Distribution for **Natcats**.
