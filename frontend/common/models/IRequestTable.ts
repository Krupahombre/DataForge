export interface IRequestTable {
  name: string;
  fields: IResultTableRecord[];
}

export interface IResultTableRecord {
  name: string;
  type: string;
  subtype: string;
}

export const defaultTable: IRequestTable = {
  name: "",
  fields: [],
};

export const defaultResultTableRecord: IResultTableRecord = {
  name: "",
  type: "",
  subtype: "",
};
