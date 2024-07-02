export default function ProductLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      <h2>
        <span className="bg-red-200 p-1 text-black font-bold">
          Product layout
        </span>
      </h2>

      {/* чак сега се вклчюва останалото съдържание */}
      {children}
    </div>
  );
}
