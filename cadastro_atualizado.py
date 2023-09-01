@classmethod
  def abrir(cls):
    cls.clientes = []
    try: 
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          #cliente = Cliente(**obj)
          cliente = Cliente(obj["_id"], obj["_nome"], obj["_email"], obj["_fone"])
          cls.clientes.append(cliente)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.clientes, arquivo, default=lambda obj: obj.__dict__)
