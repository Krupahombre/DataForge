import axios from "axios";
import { API_URL } from "../constans";
import IResponse from "../models/IResponse";

const getData = async (): Promise<IResponse> => {
  const body = {
    generators_list: ["person", "iban"],
    records: 2,
  };

  try {
    const response = await axios.post(API_URL, body);
    const result = {
      iban: response.data.iban.toString(),
      person: response.data.person.toString(),
    } as IResponse;
    return result;
  } catch (error) {
    console.error(error);
    return undefined;
  }
};

export default getData;
