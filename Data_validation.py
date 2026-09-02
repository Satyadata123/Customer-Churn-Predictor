from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional



class Churn_validation(BaseModel):
    RowNumber: Annotated[Optional[int], Field(default=None, description="Row index number")]
    CustomerId : Annotated[int, Field(..., description="enter the custumer id", gt = 0)]
    Surname : Annotated[str, Field(..., description= "enter the user  surname")]
    CreditScore : Annotated[int, Field(..., description= "enter the user creadit card score")]
    Geography : Annotated[Literal['France', 'Germany', 'Spain'], Field(..., description= "enter the custer geography")]
    Gender : Annotated[Literal["Male", "Female"], Field(..., description= "enter the custmer Gender" )]
    Age : Annotated[int, Field(..., description= "enter the custumer age ", gt=0, lt= 120)]
    Tenure : Annotated[Literal[0,1,2,3,4,5,6,7,8,9,10], Field(..., description= "customer’s duration of relationship with the company")]
    Balance : Annotated[float, Field(..., description= "The customer’s current account balance in the bank", ge= 0)]
    NumOfProducts : Annotated[Literal[1,2,3,4], Field(..., description= "How many different products/services the customer is using ")]
    HasCrCard : Annotated[Literal[0,1], Field(..., description= "does the customer have a credit card ")]
    IsActiveMember : Annotated[Literal[0,1], Field(..., description="the customer is actively using the bank’s services.")]
    EstimatedSalary : Annotated[float, Field(..., description="annual income of the customer", gt= -1)]


