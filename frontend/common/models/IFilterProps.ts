import IFilter from "./IFilter";

export default interface IFiltersProps {
  filters: IFilter[];
  setFilters: (filters: IFilter[]) => void;
}
