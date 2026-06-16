"""
Registre d'Audit Immuable (Simulation Hyperledger Fabric).
Ce module garantit que toute levée d'anonymat par un magistrat
est gravée mathématiquement et opposable à la CNIL, sans violer
le droit à l'oubli (Aucune donnée PII n'est inscrite).
"""

import hashlib
import time
from typing import Dict

class BlockchainAuditLog:
    def __init__(self):
        self.chain = []
        # Le Genesis block
        self._create_block(proof=1, previous_hash='0', data="GENESIS")

    def _create_block(self, proof: int, previous_hash: str, data: str) -> Dict:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def _hash_block(self, block: Dict) -> str:
        encoded_block = str(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def log_magistrate_decryption(self, magistrate_id: str, graph_node_hash: str) -> bool:
        """
        Enregistre de manière immuable l'acte de déchiffrement.
        Remarque RGPD: On n'inscrit JAMAIS 'Jean Dupont' dans la blockchain.
        On inscrit uniquement le Hash du Nœud et l'ID du Magistrat.
        """
        previous_block = self.chain[-1]
        previous_hash = self._hash_block(previous_block)
        
        # Payload purement technique, 100% compliant RGPD
        audit_payload = f"ACTION:DECRYPT | MAGISTRAT:{magistrate_id} | TARGET_NODE:{graph_node_hash}"
        
        # Simulation Proof of Work (basique)
        proof = 42 # Dans un vrai système, Hyperledger gère le consensus BFT
        
        self._create_block(proof, previous_hash, audit_payload)
        print(f"[AUDIT SÉCURISÉ] Action inscrite dans le bloc {len(self.chain)}. HASH: {previous_hash[:10]}...")
        return True
