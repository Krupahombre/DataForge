import IFilter from "./IFilter";
import { Dispatch, SetStateAction } from "react";

export default interface IFiltersProps {
  filters: IFilter[];
  setFilters: (filters: IFilter[]) => void;
  handleGenerate: () => void;
  numberOfRecords: number;
  setNumberOfRecords: (number) => void;
}
