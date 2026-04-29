# Computer Architecture: Pipelining Notes

Pipelining is a technique used to improve processor throughput by overlapping the execution of multiple instructions.

---

## 1. The Standard 5-Stage Pipeline
The execution of a single instruction is divided into these atomic stages:

1.  **IF (Instruction Fetch):** Fetch the instruction from memory.
2.  **ID (Instruction Decode):** Decode the instruction and read from registers.
3.  **EX (Execute):** Execute the operation in the ALU.
4.  **MEM (Memory Access):** Access data memory if necessary.
5.  **WB (Write Back):** Write results back into the register file.

[Image of 5-stage RISC pipeline execution]

---

## 2. Performance Concepts
- **Throughput:** The number of instructions completed per unit of time.
- **Latency:** The time taken for a single instruction to complete all stages.
- **Ideal Speedup:** $k$ times for a $k$-stage pipeline.

---

## 3. Pipeline Hazards
Hazards are roadblocks that prevent the pipeline from operating at full speed.

### A. Structural Hazards
Occur when two instructions attempt to use the same hardware resource (e.g., memory) simultaneously.

### B. Data Hazards
Occur when an instruction requires the result of a previous instruction that has not yet reached the Write-Back stage.
- **Solution:** **Forwarding (Bypassing)** – providing the data as soon as it is computed in the ALU.

[Image of pipeline data hazard and forwarding]

### C. Control Hazards
Caused by branch/jump instructions. The processor doesn't know which instruction to fetch next until the branch is resolved.
- **Solution:** **Branch Prediction** or **Branch Delay Slots**.

---

## 4. Mitigation Techniques Summary

| Hazard | Primary Solution |
| :--- | :--- |
| **Structural** | Increase hardware (Separate I-Cache and D-Cache) |
| **Data** | Forwarding / Bypassing |
| **Data (Hard)** | Pipeline Stalling (Adding Bubbles) |
| **Control** | Static or Dynamic Branch Prediction |
