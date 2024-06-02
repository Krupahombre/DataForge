import axios from "axios";
import { API_URL } from "../constans";
import IDisplayDataRecord from "../models/IDisplayDataRecord";
import { IRequestTable } from "../models/IRequestTable";

const getData = async (
  requestTables: IRequestTable[],
  formatFilters: string,
  numberOfRecords: number
): Promise<IDisplayDataRecord[]> => {
  const body = {
    tables: requestTables.map((table) => ({
      name: table.name,
      fields: table.fields.map((field) => ({
        name: field.name,
        type: `${field.type}:${field.subtype}`,
      })),
    })),
    records: numberOfRecords,
    format: formatFilters.toLowerCase(),
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
