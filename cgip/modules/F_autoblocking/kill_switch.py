class KillSwitch:
    """
    Kill-Switch d'application (Auto-Blocking).
    Couche Enforcement finale : coupe le pipeline ML si la gouvernance
    (Module E) déclenche un risque absolu.
    """
    def __init__(self):
        self.active = True

    def trigger(self, reason):
        self.active = False
        print(f"[KILL SWITCH ACTIVATED] {reason}")

    def check(self):
        return self.active

def enforce(decision, pipeline, kill_switch):
    if not kill_switch.check():
        raise Exception("System halted by Auto-Blocking Enforcement")
    if decision == "BLOCK":
        kill_switch.trigger("Policy violation detected in real-time stream")
        raise Exception("Pipeline blocked by Constitutional AI policy")
    if decision == "WARN":
        print("Warning: risky operation logged.")
    return pipeline
