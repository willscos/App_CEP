from app.models.cep_model import buscar_cep

def get_cep_data(cep):
    if not cep or not cep.isdigit() or len (cep) != 8:
        return{ 'erro': 'cep invalido'}
    
    data = buscar_cep(cep)

    if not data:
        return {'erro': 'O CEP NÃO FOI ENCONTRADO OU A API ESTA INDISPONIVEL'}
    
    # SE DER CERTO

    return{

        "logradouro": data.get('logradouro'),
        "bairro": data.get('bairro'),
        "cidade": data.get('cidade') or data.get('localidade'),
        "estado": data.get('uf') or data.get('estado')

    }