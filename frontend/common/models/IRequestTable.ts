export interface IRequestTable {
  name: string;
  fields: IResultTableRecord[];
}

export interface IResultTableRecord {
  name: string;
  type: string;
  subtype: string;
}
