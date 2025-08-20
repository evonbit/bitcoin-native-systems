# How to Activate UBIT Reinscription

Generations 1–4 Natcats render via the **UNAT standard**, and also via the **UBIT model** through reinscription.  

- **UNAT Rendering** requires UNAT-compatible wallets to display on-chain artwork.  
- **UBIT Rendering** displays natively in all explorers.  

When a UBIT reinscription is activated, the first valid reinscription that meets the syntax rules will render. This render is packaged with the original UNAT inscription’s satoshi. Only the first valid attempt will succeed.  

---

## How to Activate UBIT Reinscription

To reinscribe a Natcat under the UBIT model, holders must:  

1. **Reinscribe on the original Natcat inscription / satoshi.**  
2. **Include a `delegate` metadata field** pointing to the authorized parent inscription ID (`[AUTHORIZED_PARENT_INSCRIPTION_ID]`).  
3. **Include the following JSON object** inside the **undelegated content** of the inscription:  

   ```json
   {
     "tick": "natcats",
     "blk": 999999
   }
   ```

   - `tick` must be `"natcats"`.  
   - `blk` must match the **original asset’s block number**.  

---

## Validation

Only the **first reinscription** is recognized as valid. Additional attempts will not render.  

---
