export interface IErrors {
  tableNameError: boolean;
  recordNameError: boolean;
  noListItemsError: boolean;
}

export const defaultErrors: IErrors = {
  tableNameError: false,
  recordNameError: false,
  noListItemsError: false,
};
