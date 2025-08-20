# How to Inscribe a New Natcat

The mint rights for each new Natcat are allocated via lottery to the holder of a Natcat with a lower block number, as returned by the on-chain live index.

Only the holder of the authorized parent (the winning block) is able to inscribe the new Natcat. The inscription must meet the following requirements:

1. The new Natcat must be inscribed as a **child** of the authorized parent.
2. The inscription must include a **`delegate` metadata field**, set to the authorized parent’s inscription ID (`[AUTHORIZED_PARENT_INSCRIPTION_ID]`).
3. The inscription must include a JSON object inside its **undelegated content**:

   ```json
   {
     "tick": "natcats",
     "blk": 999999
   }
   ```

   - `tick` must be `"natcats"`.
   - `blk` must be the eligible Bitcoin block height.

---

## Validation

An inscription is considered valid only if it satisfies **all** of the above requirements **and is the earliest inscription to do so**.

Attempts that do not meet these conditions will:
- **Fail validation**
- **Not render**
- **Be excluded from the live index**

---

## Notes

- The **live index and mint authorization list** are published on-chain at `[placeholder inscription ID]`, which is the reference source for block winners and mint rights.
- Mints have **no expiry** and can be performed using any tool that supports **Ordinals protocol v0.21.2** or later.
