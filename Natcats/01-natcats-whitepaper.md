
[View on ordinals.com](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)  

Querying this inscription returns the canonical inscription ID and block winner for each cat, updating automatically and indefinitely as new cats are produced and inscribed by holders.  

---

## Deployment  

### 5.1 Deployment History  
On its launch, Natcats pioneered the **Unique Non-Arbitrary Token (UNAT)** standard. In August 2025, Natcats migrated to the **Bitcoin-Native Perpetual Distribution (Perpetual Distribution)** model, developed to support fully decentralized indexing, lottery-based distribution, and native rendering.  

This migration replaced reliance on third-party indexers and privileged issuers with a fully on-chain system. Under Perpetual Distribution, mint rights for new supply are allocated directly to holders via the [Authorization Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/Perpetual%20Distribution/scripts/authorization-script.py), while canonical validation and indexing are enforced through the [Indexing Script](https://github.com/evonbit/bitcoin-native-systems/blob/main/Perpetual%20Distribution/scripts/indexing-script.py) and deployment inscription.  

### 5.2 Rendering Paths  
The first four generations of Natcats render via the UNAT pathway by default, but can optionally be **reinscribed** to enable native rendering under Perpetual Distribution.  

- UNAT rendering requires UNAT-specific wallet support to display on-chain artwork.  
- Perpetual Distribution rendering works natively in all Ordinals explorers.  

Reinscription can be performed once per asset by holders. The first valid reinscription that matches the required syntax becomes the canonical Perpetual Distribution render, **permanently packaged with the original UNAT inscription**. Only the first valid reinscription will render.  

Generations **5 and beyond** render natively under Perpetual Distribution by default.  

See [How to Enable Native Render Reinscription](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md) for detailed instructions.  

---

## Status  
The latest Natcat production status — including the current block, Bits value, and whether a new generation has been triggered — can be queried via the [Natcats Index Inscription](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0).  

---

## Links  

### Project Links  
- [X / Twitter](https://x.com/dmtnatcats)  
- [Magic Eden Marketplace](https://magiceden.io/ordinals/marketplace/dmtnatcats)  
- [Discord](https://discord.gg/PaQPwWXUSz)  
- [GitHub](https://github.com/evonbit)  

### Resources  
- Viewer (Explore cats + download image file)  
- [Live on-chain index](https://ordinals.com/inscription/765eadb692a430b2ea43c34e6f6fdde6490651fd5496ebdb9946487e1e7337f4i0)  
- [Traits list](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/02-natcats-traits.md)  
- [How to mint newly issued Natcats](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/03-natcats-perpetual-distribution-upgrade.md)  
- [How to enable native render reinscription](https://github.com/evonbit/bitcoin-native-systems/blob/main/Natcats/04-how-to-enable-native-render-reinscription.md)  
- [Perpetual Distribution documentation](https://github.com/evonbit/bitcoin-native-systems/blob/main/Perpetual%20Distribution/01-about-perpetual-distribution.md)  

### Related Links  
- [Ordinals Documentation](https://docs.ordinals.com/)  
- [Digital Matter Theory](https://digital-matter-theory.gitbook.io/digital-matter-theory)  
