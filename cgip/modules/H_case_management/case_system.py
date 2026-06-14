class Case:
    """
    Case Management System (Investigation Workspace).
    Maintient l'état d'une investigation, agrège les alertes GNN et permet la traçabilité humaine.
    """
    def __init__(self, case_id):
        self.id = case_id
        self.events = []
        self.status = "OPEN"

    def add_event(self, event):
        self.events.append(event)

    def close(self):
        self.status = "CLOSED"

    def audit_trail(self):
        return {
            "case_id": self.id,
            "status": self.status,
            "event_count": len(self.events)
        }
