from pydantic import BaseModel, Field
from typing import Optional, Literal
import uuid

class OneriSemasi(BaseModel):
    recommendation_id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Önerinin benzersiz kimliği")
    order_id: str = Field(..., description="Sipariş kimliği")
    policy_version: str = Field(..., description="Kullanılan politika sürümünün tarihi veya kimliği")
    
    action: Literal[
        'store_credit', 'partial_refund', 'replacement', 
        'full_refund', 'escalate_to_human', 'no_action'
    ] = Field(..., description="Uygulanacak aksiyon")
    
    amount_percent: Optional[float] = Field(None, description="Önerilen tutar yüzdesi")
    justification: str = Field(..., description="Politika maddesine dayanan kısa gerekçe")
    evidence_quality: Literal['high', 'low', 'none'] = Field(..., description="Kanıt kalitesi")
    
    policy_conflict_detected: bool = Field(..., description="Girdilerde eski veya çelişen politika tespit edildi mi")
    policy_conflict_note: Optional[str] = Field(None, description="Çelişki açıklaması")
    
    confidence: float = Field(..., ge=0.0, le=1.0, description="Modelin öneriye ilişkin güven değeri (0-1 arası)")
    requires_escalation: bool = Field(..., description="Önerinin doğrudan insana yönlendirilmesi gerekip gerekmediği")