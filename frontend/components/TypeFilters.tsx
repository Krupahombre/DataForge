import React from "react";
import FormatFilterBox from "./FormatFilterBox";
import styles from "../styles/Home.module.css";
import IFiltersProps from "../common/models/IFilterProps";

const FormatFilters: React.FC<IFiltersProps> = ({ filters, setFilters }) => {
  const handleToggle = (key: number) => {
    const newFilters = [...filters];
    newFilters[key] = {
      ...newFilters[key],
      selected: !newFilters[key].selected,
    };
    setFilters(newFilters);
  };

  return (
    <div className={styles.chooseFilterWrapper}>
      <h1 className={styles.chooseFiltersLabel}>Choose the types of data:</h1>
      <div className={styles.chooseFilterBox}>
        {filters.map((filter, key) => (
          <FormatFilterBox
            key={key}
            columnName={filter.name}
            selectedState={filter.selected}
            changeSelectedState={() => handleToggle(key)}
          />
        ))}
      </div>
    </div>
  );
};

export default FormatFilters;
