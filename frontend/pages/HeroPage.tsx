import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import FormatFilters from "../components/FormatFilters";
import TypeFilters from "../components/TypeFilters";
import IFilter from "../common/models/IFilter";
import type { NextPage } from "next";
import { useRouter } from "next/router";

const HeroPage: NextPage = () => {
  const [formatFilters, setFormatFilters] = useState<IFilter[]>(
    [] as IFilter[]
  );
  const [typeFilters, setTypeFilters] = useState<IFilter[]>([] as IFilter[]);
  const router = useRouter();

  const handleGenerate = () => {
    console.log(typeFilters, formatFilters);
    const type = typeFilters.filter((column) => column.selected);
    const format = formatFilters.find((type) => type.selected)?.name;

    if (isFormFilled()) {
      const queryString =
        `a=b&format=${format}&` +
        type.map((value) => `type=${value.name}`).join("&");
      router.push(`/ResultDisplayPage?${queryString}`);
    }
  };

  useEffect(() => {
    setFormatFilters(getFormat());
    setTypeFilters(getTypes());
  }, []);

  const getTypes = (): IFilter[] => {
    return [
      { name: "person", selected: false },
      { name: "iban", selected: false },
    ];
  };

  const getFormat = (): IFilter[] => {
    return [
      { name: "JSON", selected: false },
      { name: "MySQL", selected: false },
    ];
  };

  const isFormFilled = () => {
    return (
      formatFilters.some((column) => column.selected) &&
      typeFilters.some((type) => type.selected)
    );
  };

  return (
    <div className={styles.heroBox}>
      <h1 className={styles.heroLabel}>Data Forge</h1>
      <h2 className={styles.heroSubLabel}>Generate your data!</h2>
      <div className={styles.userInputWrapper}>
        <TypeFilters filters={typeFilters} setFilters={setTypeFilters} />
        <FormatFilters filters={formatFilters} setFilters={setFormatFilters} />
      </div>
      <div className={styles.generateBottonBox}>
        <button onClick={handleGenerate} className={styles.generateButton}>
          Generate
        </button>
      </div>
    </div>
  );
};
export default HeroPage;
