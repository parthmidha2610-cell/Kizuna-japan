// app/page.tsx
'use client';
import { useEffect, useState } from 'react';
import { fetchFullCatalog } from '@/lib/dataLoader';
import { CatalogTitle } from '@/types/catalog';

export default function Home() {
  const [animeList, setAnimeList] = useState<CatalogTitle[]>([]);

  useEffect(() => {
    fetchFullCatalog().then((data) => {
      console.log("Fetched Data:", data);
      setAnimeList(data);
    });
  }, []);

  return (
    <div className="p-10 font-sans">
      <h1 className="text-2xl font-bold text-pink-600 mb-4">KIZUNA SYSTEM CHECK</h1>
      {animeList.length === 0 ? (
        <p>Loading database or database is empty...</p>
      ) : (
        <ul className="space-y-2">
          {animeList.map((anime) => (
            <li key={anime.id} className="p-4 border rounded shadow-sm">
              <strong>{anime.name}</strong> - Fame Tier: {anime.india_fame_tier}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}