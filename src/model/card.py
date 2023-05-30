class Card:
  def __init__(self, name: str, cost: int, power: int, ability: str,
               url: str, status: str, source: str, variants: list[str]) -> None:
    self.name = name
    self.cost = cost
    self.power = power
    self.ability = ability
    self.url = url
    self.status = status
    self.source = source
    self.variants = variants
