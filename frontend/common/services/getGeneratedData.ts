import axios from "axios";
import { API_URL } from "../constans";
import IDisplayDataRecord from "../models/IDisplayDataRecord";

const getData = async (
  format: string,
  types: string[]
): Promise<IDisplayDataRecord[]> => {
  console.log(types);
  const types_ = ["person", "iban"];

  const body = {
    generators_list: types,
    records: 2,
  };

  const response = await axios.post(API_URL, body);

  const mappedResponse: IDisplayDataRecord[] = Object.keys(response.data).map(
    (fieldname) => ({
      name: fieldname,
      response: response.data[fieldname],
    })
  );

  return mappedResponse;
};

export default getData;
