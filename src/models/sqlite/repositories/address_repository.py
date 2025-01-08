from src.models.sqlite.entities.address import Address
from src.models.sqlite.interfaces.address import IAddressRepository


class AddressRepository(IAddressRepository):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def insert_address(self, user_id: int, rua: str, numero: str, complemento: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        with self.__db_connection as database:
            try:
                address = Address(
                    user_id=user_id,
                    rua=rua,
                    numero=numero,
                    complemento=complemento,
                    bairro=bairro,
                    cidade=cidade,
                    estado=estado,
                    cep=cep
                )
                database.session.add(address)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e