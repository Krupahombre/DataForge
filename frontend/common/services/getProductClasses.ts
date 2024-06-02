import axios from "axios";
import { API_URL } from "../constans";
import { IProductClass } from "../models/IProductClass";

export const getProductClasses = async (): Promise<IProductClass[]> => {
  const response = await axios.get(API_URL + "/get-generators");

  const data = response.data;
  const productClasses: IProductClass[] = Object.keys(data).map((key) => ({
    name: key,
    fields: data[key],
  }));

  return productClasses;
};
