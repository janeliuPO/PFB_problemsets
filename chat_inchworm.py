#!/usr/bin/env python3
import sys
import math

def shannon_entropy(seq):
    """Compute Shannon entropy to 2 decimal places."""
    length = len(seq)
    freqs = {}
    for base in seq:
        freqs[base] = freqs.get(base, 0) + 1
    entropy = 0.0
    for count in freqs.values():
        p = count / length
        entropy -= p * math.log2(p)
    return round(entropy, 2)

def load_kmers(fastq_file, k):
    """Count kmers in a FASTQ file and compute entropy."""
    kmer_counts = {}
    with open(fastq_file, 'r') as f:
        for i, line in enumerate(f):
            if i % 4 == 1:
                seq = line.strip().upper()
                for j in range(len(seq) - k + 1):
                    kmer = seq[j:j+k]
                    kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1
    kmer_dict = {}
    for kmer, count in kmer_counts.items():
        kmer_dict[kmer] = (count, shannon_entropy(kmer))
    return kmer_dict

def find_extension(kmers, current_kmer, direction="right"):
    """Find best extension kmer sharing k-1 overlap."""
    k = len(current_kmer)
    best = None
    best_count = 0
    if direction == "right":
        suffix = current_kmer[1:]
        for kmer, (count, _) in kmers.items():
            if kmer.startswith(suffix) and count > best_count:
                best = kmer
                best_count = count
    else:
        prefix = current_kmer[:-1]
        for kmer, (count, _) in kmers.items():
            if kmer.endswith(prefix) and count > best_count:
                best = kmer
                best_count = count
    return best

def assemble_contigs(kmers, entropy_min):
    """Assemble contigs from kmers, starting from dominant high-entropy kmers."""
    contigs = []
    while True:
        # Pick best seed that meets entropy threshold
        candidates = [(k, v[0], v[1]) for k, v in kmers.items() if v[1] >= entropy_min]
        if not candidates:
            break
        seed = max(candidates, key=lambda x: x[1])[0]
        contig = seed
        used = {seed}
        del kmers[seed]

        # Extend to the right
        while True:
            nxt = find_extension(kmers, contig[-len(seed):], "right")
            if not nxt:
                break
            contig += nxt[-1]
            used.add(nxt)
            del kmers[nxt]

        # Extend to the left
        while True:
            nxt = find_extension(kmers, contig[:len(seed)], "left")
            if not nxt:
                break
            contig = nxt[0] + contig
            used.add(nxt)
            del kmers[nxt]

        contigs.append(contig)

    return contigs

def main():
    if len(sys.argv) < 4:
        print("Usage: python assembler.py <fastq_file> <kmer_size> <min_entropy>")
        sys.exit(1)

    fastq_file = sys.argv[1]
    k = int(sys.argv[2])
    min_entropy = float(sys.argv[3])

    kmers = load_kmers(fastq_file, k)
    contigs = assemble_contigs(kmers, min_entropy)

    print("\nAssembled contigs:")
    for i, contig in enumerate(contigs, 1):
        print(f">contig_{i}\n{contig}")

if __name__ == "__main__":
    main()
