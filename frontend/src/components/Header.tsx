import Image from "next/image";
import Link from "next/link";

export default function Header() {
  return (
    <header className="w-full h-16 bg-[#12A19A]">
      <nav className="max-w-7xl mx-auto h-full px-6 flex items-center justify-between">

        <Link href="/" className="flex items-center gap-2">
          <Image
            src="./logo.svg"
            alt="Lucro Rural"
            width={120}
            height={32}
            priority
          />
        </Link>

        <ul className="flex gap-6 text-white">
          <li>
            <Link className="transition-colors hover:text-[#0E7C77]" href="/">
              Home
            </Link>
          </li>
          <li>
            <Link className="transition-colors hover:text-[#0E7C77]" href="/fornecedores">
              Fornecedores
            </Link>
          </li>
          <li>
            <Link className="transition-colors hover:text-[#0E7C77]" href="/contas-a-pagar">
              Notas Fiscais
            </Link>
          </li>
        </ul>

      </nav>
    </header>
  );
}
