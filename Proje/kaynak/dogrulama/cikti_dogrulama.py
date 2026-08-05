from kaynak.karar_motoru.sema import OneriSemasi

class CiktiDogrulayici:
    def __init__(self, guven_esigi: float = 0.85):
        self.guven_esigi = guven_esigi

    def politika_siniri_kontrolu(self, oneri: OneriSemasi) -> OneriSemasi:
        """
        Üretilen önerinin politika sınırlarını aşıp aşmadığını koddan bağımsız olarak doğrular.
        Sınır aşımı varsa, öneriyi insan onayına (escalation) zorlar.
        """
        
        # 1. Düşük veya belirsiz kanıt kontrolü
        if oneri.evidence_quality in ['low', 'none'] and oneri.action != 'no_action':
            oneri.requires_escalation = True
            oneri.justification += " [SİSTEM NOTU: Yetersiz kanıt nedeniyle insan onayına yönlendirildi.]"
            oneri.action = 'escalate_to_human'
            
        # 2. Güven değeri kontrolü
        if oneri.confidence < self.guven_esigi:
            oneri.requires_escalation = True
            
        # 3. Politika çelişmesi kontrolü
        if oneri.policy_conflict_detected:
            oneri.requires_escalation = True
            oneri.action = 'escalate_to_human'
            
        return oneri