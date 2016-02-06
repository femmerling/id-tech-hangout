namespace py auth
namespace java auth
namespace php auth
namespace rb auth

typedef i32 int

exception TokenNotValidException{
    1: int error_code,
    2: string message
}

exception UserAlreadyExistException{
    1: int error_code,
    2: string message
}

service AuthenticationService
{
    string authenticate(1: string access_token) throws (1: TokenNotValidException e),
    string register_client(1: string name, 2:string email) throws (1: UserAlreadyExistException e)
}